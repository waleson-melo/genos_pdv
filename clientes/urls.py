from django.urls import path

from .views import Cadastrar, Alterar, Listar


urlpatterns = [
    path('cadastrar/', Cadastrar.as_view(), name='clientes-cadastrar'),
    path('listar/', Listar.as_view(), name='clientes-listar'),
    path('alterar/<int:pk>', Alterar.as_view(), name='clientes-alterar'),
]