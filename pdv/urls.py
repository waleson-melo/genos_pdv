from django.urls import path

from .views import CadastroVenda


urlpatterns = [
    path('cadastrar/', CadastroVenda, name='pdv-cadastro'),
]
