from django.urls import path

from .views import Cadastrar, Alterar, Listar


urlpatterns = [
    path('cadastrar/', Cadastrar.as_view(), name='fornecedores-cadastrar'),
    path('alterar/<int:pk>', Alterar.as_view(), name='fornecedores-alterar'),
    path('listar/', Listar.as_view(), name='fornecedores-listar'),
]
