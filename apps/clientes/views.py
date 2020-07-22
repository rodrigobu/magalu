from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from apps.clientes.models import Clientes

class CadastroClientes(CreateView):
    model = Clientes
    template_name = 'clientes/cadastro.html'
    fields = ('__all__')
    success_url =  reverse_lazy('clientes.lista')

cadastro = CadastroClientes.as_view()


class EdicaoClientes(UpdateView):
    model = Clientes
    template_name = 'clientes/cadastro.html'
    fields = ('__all__')
    success_url =  reverse_lazy('clientes.lista')
    
edicao = EdicaoClientes.as_view()


class ListarClientes(ListView):
    model = Clientes
    template_name = 'clientes/lista.html'
    context_object_name = 'clientes'
    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clientes = self.get_queryset().order_by('name')
        page = self.request.GET.get('page')
        paginator = Paginator(clientes, self.paginate_by)
        try:
            clientes = paginator.page(page)
        except PageNotAnInteger:
            clientes = paginator.page(1)
        except EmptyPage:
            clientes = paginator.page(paginator.num_pages)
        context['clientes'] = clientes
        return context

lista = ListarClientes.as_view()


class DeletarClientes(DeleteView):
    model = Clientes
    template_name = 'clientes/delete.html'
    success_url =  reverse_lazy('clientes.lista')

delete = DeletarClientes.as_view()