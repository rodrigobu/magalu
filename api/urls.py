from django.urls import include, path
from api import views

from rest_framework import routers


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [

    path('clients/', views.ClientApiView.as_view()),
    path('clients/<pk>/', views.ClientApiView.as_view()),
    path('clients/favorites/<pk>/', views.FavoritosApiView.as_view()),

    path('products/', views.ProdutosApiView.as_view()),
    path('products/<pk>/', views.ProdutosApiView.as_view()),
   




]