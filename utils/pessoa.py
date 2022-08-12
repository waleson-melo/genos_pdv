from django.db import models


class Pessoa():
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    data_cadastro = models.DateField('Dada de Cadastro', auto_now_add=True)
