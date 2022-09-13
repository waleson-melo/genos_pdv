from django.urls import path

from .views import CadastroVenda, AlterarVenda, ListarVenda


urlpatterns = [
    path('listar/', ListarVenda.as_view(), name='vendas-listar'),
    path('cadastrar/', CadastroVenda, name='vendas-cadastrar'),
    path('alterar/<int:pk>', AlterarVenda, name='vendas-alterar'),
]
