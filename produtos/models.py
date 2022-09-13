from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    estoque = models.IntegerField()
    valor = models.FloatField()
    
    def __str__(self):
        return '{}-{}'.format(self.nome, self.valor)
