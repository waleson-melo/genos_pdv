from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.forms.models import inlineformset_factory

from .models import Venda, ItemVenda
from .forms import VendaForm, ItemVendaForm


def CadastroVenda(request):
    if request.method == 'GET':
        form = VendaForm()
        form_itemvenda_factory = inlineformset_factory(Venda, ItemVenda, form=ItemVendaForm, extra=4)
        form_itemvenda = form_itemvenda_factory()
        context = {
            'form': form,
            'form_itemvenda': form_itemvenda,
        }
        return render(request, 'paginas/form_venda.html', context=context)
    elif request.method == 'POST':
        form = VendaForm(request.POST)
        form_itemvenda_factory = inlineformset_factory(Venda, ItemVenda, form=ItemVendaForm)
        form_itemvenda = form_itemvenda_factory(request.POST)
        
        if form.is_valid() and form_itemvenda.is_valid():
            venda = form.save()
            form_itemvenda.instance = venda
            form_itemvenda.save()
            return redirect(reverse('vendas-listar'))
        else:
            context = {
                'form': form,
                'form_itemvenda': form_itemvenda,
            }
            return render(request, 'paginas/form_venda.html', context=context)


def AlterarVenda(request, pk):
    if request.method == 'GET':
        object = Venda.objects.filter(id=pk).first()
        if object is None:
            return redirect(reverse('paginas/form_venda.html'))
        
        form = VendaForm(instance=object)
        form_itemvenda_factory = inlineformset_factory(Venda, ItemVenda, form=ItemVendaForm, extra=1)
        form_itemvenda = form_itemvenda_factory(instance=object)
        context = {
            'form': form,
            'form_itemvenda': form_itemvenda,
        }
        return render(request, 'paginas/form_venda.html', context=context)
    elif request.method == 'POST':
        object = Venda.objects.filter(id=pk).first()
        if object is None:
            return redirect(reverse('paginas/form_venda.html'))

        form = VendaForm(request.POST, instance=object)
        form_itemvenda_factory = inlineformset_factory(Venda, ItemVenda, form=ItemVendaForm)
        form_itemvenda = form_itemvenda_factory(request.POST, instance=object)
        
        if form.is_valid() and form_itemvenda.is_valid():
            venda = form.save()
            form_itemvenda.instance = venda
            form_itemvenda.save()
            return redirect(reverse('users-listar'))
        else:
            context = {
                'form': form,
                'form_itemvenda': form_itemvenda,
            }
            return render(request, 'paginas/form_venda.html', context=context)


class ListarVenda(ListView):
    template_name = 'paginas/list_vendas.html'
    model = Venda
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Listar Vendas'
        
        return context


# class CadastroVenda(CreateView):
#     template_name = 'paginas/form_venda.html'
#     form_class = VendaForm
#     model = Venda
#     form_itemvenda_factory = inlineformset_factory(Venda, ItemVenda, form=ItemVendaForm, extra=1)
#     form_itemvenda = form_itemvenda_factory()
#     success_url = reverse_lazy('users-listar')
    
#     def form_valid(self, form):
#         if self.request.method == 'POST':
#             form = VendaForm(self.request.POST)
#             self.form_itemvenda = self.form_itemvenda_factory(self.request.POST)
#             print(self.form_itemvenda.is_valid())
#             if form.is_valid() and self.form_itemvenda.is_valid():
#                 venda = form.save()
#                 self.form_itemvenda.instance = venda
#                 self.form_itemvenda.save()

#         return super().form_valid(form)
    
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['titulo_pagina'] = 'Cadastrar Venda'
#         context['form_itemvenda'] = self.form_itemvenda
        
#         return context
