from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Categoria, Produto


class CadastroCategoria(CreateView):
    template_name = 'paginas/form_categoria.html'
    model = Categoria
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('produtos-categoria-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Cadastrar Categoria'
        
        return context


class CadastroProduto(CreateView):
    template_name = 'paginas/form_produto.html'
    model = Produto
    fields = ['nome', 'descricao', 'categoria', 'estoque']
    success_url = reverse_lazy('produtos-produto-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Cadastrar Produto'
        
        return context


class AlterarCategoria(UpdateView):
    template_name = 'paginas/form_categoria.html'
    model = Categoria
    fields = ['nome', 'descricao']
    success_url = reverse_lazy('produtos-categoria-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Alterar Categoria'
        
        return context


class AlterarProduto(UpdateView):
    template_name = 'paginas/form_produto.html'
    model = Produto
    fields = ['nome', 'descricao', 'categoria', 'estoque']
    success_url = reverse_lazy('produtos-produto-listar')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Alterar Produto'
        
        return context


class ListarCategorias(ListView):
    template_name = 'paginas/list_categoria.html'
    model = Categoria
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Listar Categorias'
        
        return context


class ListarProdutos(ListView):
    template_name = 'paginas/list_produto.html'
    model = Produto
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pagina'] = 'Listar Produtos'
        
        return context
