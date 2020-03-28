from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

    class Meta:
        abstract = True

class Contato(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)

    class Meta:
        abstract = True

class Remetente(Contato, Address):
    cnpj = models.CharField(max_length=15)

class Destinatario(Contato, Address):
    cpf = models.CharField(max_length=15)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    age = models.DateField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True, max_length=60)

    def __str__(self):
        return self.user.username
