from django.urls import path

from apps.clientes.views import cadastro, edicao, lista, delete

urlpatterns = [
    path('cadastro/',
        cadastro,
        name='clientes.cadastro'
    ),

    path('editar/<pk>/',
        edicao,
        name='clientes.edicao'
    ),

    path('',
        lista,
        name='clientes.lista'
    ),

    path('delete/<pk>/',
        delete,
        name='clientes.delete'
    )
]