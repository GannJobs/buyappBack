from django.db import models
from loja.models import Loja

# Create your models here.
class Categorias(models.Model):
    Nome = models.CharField(max_length=20)
    Descricao = models.CharField(max_length=200)
    Loja = models.ForeignKey(Loja, on_delete=models.CASCADE, blank=True)