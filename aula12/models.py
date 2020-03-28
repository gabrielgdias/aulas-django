from django.db import models


class Automovel(models.Model):
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=10)
    slug = models.CharField(max_length=40)