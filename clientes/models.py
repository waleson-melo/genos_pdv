from django.db import models


class Cliente(models.Model):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)
    
    def __str__(self):
        return 'Cliente: {}'.format(self.nome)
