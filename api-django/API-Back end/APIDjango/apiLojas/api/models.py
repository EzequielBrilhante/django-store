from django.db import models

# Create your models here.

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField(null=False)
    endereco = models.CharField(max_length=100, null=False)

def __str__(self):
    return self.titulo

