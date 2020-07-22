from django.urls import path

from apps.produtos.views import cadastro, edicao, lista, delete

urlpatterns = [
    path('cadastro/',
        cadastro,
        name='produtos.cadastro'
    ),

    path('edicao/<pk>/',
        edicao,
        name='produtos.edicao'
    ),

    path('',
        lista,
        name='produtos.lista'
    ),

    path('delete/<pk>/',
        delete,
        name='produtos.delete'
    ),
]