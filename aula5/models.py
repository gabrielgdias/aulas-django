from django.db import models
from pytz.tzfile import _NULL

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    twitter  = models.URLField()
    data_nascimento = models.DateField(null=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    texto = models.TextField()
    categorias = models.ManyToManyField(Categoria, related_name="posts")

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    autor = models.CharField(max_length=30)
    comentario = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return self.autor

class Carrinho(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    usuario = models.CharField(max_length=255)

    @property
    def total(self):
        total = self.produto_set.all().aggregate(models.Sum('preco'))
        return total['preco__sum']


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.FloatField()
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
