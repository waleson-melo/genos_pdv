from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Fornecedor


class Cadastrar(CreateView):
    template_name = 'paginas/form_fornecedor.html'
    model = Fornecedor
    fields = ['cpf', 'nome', 'telefone', 'email']
    success_url = reverse_lazy('fornecedores-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Cadastrar Fornecedor'
        
        return context


class Alterar(UpdateView):
    template_name = 'paginas/form_fornecedor.html'
    model = Fornecedor
    fields = ['cpf', 'nome', 'telefone', 'email']
    success_url = reverse_lazy('fornecedores-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Alterar Fornecedor'
        
        return context


class Listar(ListView):
    template_name = 'paginas/list_fornecedores.html'
    model = Fornecedor
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Listar Fornecedores'
        
        return context
