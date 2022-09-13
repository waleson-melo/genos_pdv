from django import forms

from .models import Venda, ItemVenda


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'usuario', 'descricao', 'total']


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['venda', 'produto', 'quantidade', 'total']
        
