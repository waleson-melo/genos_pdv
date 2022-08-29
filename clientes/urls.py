from django.urls import path

from .views import Cadastrar


urlpatterns = [
    path('cadastrar/', Cadastrar.as_view(), name='clientes-cadastrar'),
]