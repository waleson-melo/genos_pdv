from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import User


class Cadastrar(CreateView):
    template_name = 'paginas/form_cadastro_user.html'
    model = User
    fields = ['email', 'username', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('users-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Cadastrar Usuário'
        
        return context


class Alterar(UpdateView):
    template_name = 'paginas/form_alterar_user.html'
    model = User
    fields = ['email', 'username', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('users-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Alterar Usuário'
        
        return context


class Listar(ListView):
    template_name = 'paginas/list_user.html'
    model = User
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Listar Usuario'
        
        return context
