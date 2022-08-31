from django.urls import path

from .views import CadastroCategoria, CadastroProduto, AlterarCategoria
from .views import AlterarProduto, ListarCategorias, ListarProdutos


urlpatterns = [
    path('cadastrar/categoria/', CadastroCategoria.as_view(),
        name='produtos-categoria-cadastrar'),
    path('cadastrar/produto/', CadastroProduto.as_view(),
        name='produtos-produto-cadastrar'),
    path('alterar/categoria/<int:pk>/', AlterarCategoria.as_view(),
        name='produtos-categoria-alterar'),
    path('alterar/produto/<int:pk>/', AlterarProduto.as_view(),
        name='produtos-produto-alterar'),
    path('listar/categorias/', ListarCategorias.as_view(),
        name='produtos-categoria-listar'),
    path('listar/produtos/', ListarProdutos.as_view(),
        name='produtos-produto-listar'),
]
