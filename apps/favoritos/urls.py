from django.urls import path

from apps.favoritos.views import cadastro, edicao, lista, lista_favoritos, delete

urlpatterns = [
    path('cadastro/',
        cadastro,
        name='favoritos.cadastro'
    ),

    path('editar/<pk>/',
        edicao,
        name='favoritos.edicao'
    ),

    path('',
        lista,
        name='favoritos.lista'
    ),

    path('<pk>/',
        lista_favoritos,
        name='favoritos.lista_favoritos'
    ),

    path('delete/<pk>/',
        delete,
        name='favoritos.delete'
    )
]