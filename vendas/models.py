from django.db import models

from produtos.models import Produto
from clientes.models import Cliente
from users.models import User


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    items = models.ManyToManyField(Produto, through='ItemVenda')
    descricao = models.TextField(max_length=100, blank=True, null=True)
    total = models.FloatField()
    
    def __str__(self):
        return '{}: {}'.format(self.pk, self.cliente.nome)


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    total = models.FloatField()
