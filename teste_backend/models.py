from django.db import models


class Campos(models.Model):
    tipo = models.CharField(max_length=2)
    data = models.CharField(max_length=9)
    valor = models.CharField(max_length=11)
    cpf = models.CharField(max_length=12)
    cartao = models.CharField(max_length=13)
    hora = models.CharField(max_length=7)
    dono_loja = models.CharField(max_length=15)
    nome_loja = models.CharField(max_length=20)
