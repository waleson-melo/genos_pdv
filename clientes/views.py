from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Cliente


class Cadastrar(CreateView):
    template_name = 'paginas/form_cadastro_cliente.html'
    model = Cliente
    fields = ['cpf', 'nome', 'telefone', 'email']
    success_url = reverse_lazy('clientes-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Cadastrar Cliente'
        
        return context


class Alterar(UpdateView):
    template_name = 'paginas/form_alterar_cliente.html'
    model = Cliente
    fields = ['cpf', 'nome', 'telefone', 'email']
    success_url = reverse_lazy('clientes-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Cadastrar Cliente'
        
        return context


class Listar(ListView):
    template_name = 'paginas/list_cliente.html'
    model = Cliente
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Listar Cliente'
        
        return context
