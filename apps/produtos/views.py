from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy

from apps.produtos.models import Produtos


class CadastroProdutos(CreateView):
    model = Produtos
    template_name = 'produtos/cadastro.html'
    fields = ('price', 'image', 'brand', 'title')
    success_url = reverse_lazy('produtos.lista')

cadastro = CadastroProdutos.as_view()


class EdicaoProdutos(UpdateView):
    model = Produtos
    template_name = 'produtos/cadastro.html'
    fields = ('price', 'image', 'brand', 'title')
    success_url =  reverse_lazy('produtos.lista')

edicao = EdicaoProdutos.as_view()


class DeletarProdutos(DeleteView):
    model = Produtos
    template_name = 'produtos/delete.html'
    success_url =  reverse_lazy('produtos.lista')

delete = DeletarProdutos.as_view()

class ListarProdutos(ListView):
    model = Produtos
    template_name = 'produtos/lista.html'
    context_object_name = 'produtos'
    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produtos = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(produtos, self.paginate_by)
        try:
            produtos = paginator.page(page)
        except PageNotAnInteger:
            produtos = paginator.page(1)
        except EmptyPage:
            produtos = paginator.page(paginator.num_pages)
        context['produtos'] = produtos
        return context

lista = ListarProdutos.as_view()