from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.forms.models import inlineformset_factory

from vendas.models import Venda, ItemVenda
from vendas.forms import VendaForm, ItemVendaForm


def CadastroVenda(request):
    if request.method == 'GET':
        form = VendaForm()
        form_itemvenda_factory = inlineformset_factory(Venda, ItemVenda, form=ItemVendaForm, extra=4)
        form_itemvenda = form_itemvenda_factory()
        context = {
            'form': form,
            'form_itemvenda': form_itemvenda,
            'titulo_pagina': 'Genos PDV',
        }
        return render(request, 'paginas/form_pdv.html', context=context)
    elif request.method == 'POST':
        form = VendaForm(request.POST)
        form_itemvenda_factory = inlineformset_factory(Venda, ItemVenda, form=ItemVendaForm)
        form_itemvenda = form_itemvenda_factory(request.POST)
        
        if form.is_valid() and form_itemvenda.is_valid():
            venda = form.save()
            form_itemvenda.instance = venda
            form_itemvenda.save()
            return redirect(reverse('pdv-cadastro'))
        else:
            context = {
                'form': form,
                'form_itemvenda': form_itemvenda,
            }
            return render(request, 'paginas/form_pdv.html', context=context)
