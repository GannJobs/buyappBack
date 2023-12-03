from django.db import models
from user.models import Usuario

# Create your models here.
class Loja(models.Model):
    Nome = models.CharField(max_length=20)
    CEP = models.CharField(max_length=20)
    ContactNumber = models.CharField(max_length=20)
    Descricao = models.CharField(max_length=200)
    img = models.CharField(max_length=200, default='#')
    Dono = models.OneToOneField(Usuario, on_delete=models.CASCADE)