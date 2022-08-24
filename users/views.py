from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import User


class Cadastrar(CreateView):
    template_name = 'paginas/form_cadastro_user.html'
    model = User
    fields = ['email', 'username', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('users-cadastrar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Cadastrar Usuario'
        
        return context
