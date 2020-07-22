from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from apps.favoritos.models import Favoritos

class CadastroFavoritos(CreateView):
    model = Favoritos
    template_name = 'favoritos/cadastro.html'
    fields = ('__all__')
    success_url =  reverse_lazy('favoritos.lista')

cadastro = CadastroFavoritos.as_view()


class EdicaoFavoritos(UpdateView):
    model = Favoritos
    template_name = 'favoritos/cadastro.html'
    fields = ('__all__')
    success_url =  reverse_lazy('favoritos.lista')
    
edicao = EdicaoFavoritos.as_view()



class ListarFavoritos(ListView):
    model = Favoritos
    template_name = 'favoritos/lista_favoritos.html'
    context_object_name = 'favoritos'
    paginate_by = 5

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        favoritos = Favoritos.objects.filter(client_id=pk)
        return favoritos


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favoritos = self.get_queryset()
        nome = favoritos[0].client.name
        page = self.request.GET.get('page')
        paginator = Paginator(favoritos, self.paginate_by)
        try:
            favoritos = paginator.page(page)
        except PageNotAnInteger:
            favoritos = paginator.page(1)
        except EmptyPage:
            favoritos = paginator.page(paginator.num_pages)
        context['favoritos'] = favoritos
        context['nome_cliente'] = nome.title()
        return context

lista_favoritos = ListarFavoritos.as_view()


class ListarClientesFavoritos(ListView):
    model = Favoritos
    template_name = 'favoritos/lista.html'
    context_object_name = 'favoritos'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favoritos = self.get_queryset().distinct('client')
        favoritos = favoritos.order_by('client')
        page = self.request.GET.get('page')
        paginator = Paginator(favoritos, self.paginate_by)
        try:
            favoritos = paginator.page(page)
        except PageNotAnInteger:
            favoritos = paginator.page(1)
        except EmptyPage:
            favoritos = paginator.page(paginator.num_pages)
        context['favoritos'] = favoritos
        return context

lista = ListarClientesFavoritos.as_view()




class DeletarFavoritos(DeleteView):
    model = Favoritos
    template_name = 'favoritos/delete.html'
    success_url =  reverse_lazy('favoritos.lista')

delete = DeletarFavoritos.as_view()