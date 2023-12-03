from django.db import models
from categorias.models import Categorias
# Create your models here.
class Produto(models.Model):
    Nome = models.CharField(max_length=20)
    Valor = models.CharField(max_length=20)
    Marca = models.CharField(max_length=20)
    img = models.CharField(max_length=200, default='#')
    Categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)