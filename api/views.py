from django.http import Http404
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import ClientesSerializer, ProdutosSerializer, FavoritosSerializer

from apps.clientes.models import Clientes
from apps.produtos.models import Produtos
from apps.favoritos.models import Favoritos


class ProdutosApiView(APIView):

    def get_object(self, pk):
        if not pk:
           return Produtos.objects.all()
        try:
            return Produtos.objects.get(pk=pk)
        except Produtos.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None):
        produtos = self.get_object(pk)
        return Response(produtos.values())

    def post(self, request):
        serializer = ProdutosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
class ClientApiView(APIView):

    def get_object_favoritos(self, client_id):
        return Favoritos.objects.filter(client_id=client_id)

    def get_object(self, pk):
        if not pk:
            return Clientes.objects.all()
        try:
            return Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None, format=None):
        
        clientes = self.get_object(pk)

        content = []
        for client in clientes:
            c = {
                'id': client.id,
                'name': client.name,
                'cpf': client.cpf,
                'address': client.address,
                'email': client.email,

            }

            fav_list = []
            favorito = self.get_object_favoritos(client.id)

            for fav in favorito:
                favorites_dict = {
                    'id': fav.id,
                    'produtct_id': fav.product.id,
                    'title': fav.product.title,
                    'brand': fav.product.brand,
                    'price': fav.product.price,
                    'image': fav.product.image,
                    'review_score': fav.product.review_score 
                }
                fav_list.append(favorites_dict)

            content.append(c)
            c['favorite'] = fav_list

        return Response(content)
    
    def post(self, request):
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        clientes = self.get_object(pk)
        serializer = ClientesSerializer(clientes, data=request.data)
        favorite = request.data['favorite']
        if serializer.is_valid():
            if len(favorite) > 0:
                favoritos = Favoritos()
                for fav in favorite:
                    for k, v in fav.items():
                        favoritos = Favoritos()
                        favoritos.client_id = clientes.id
                        if k == 'id':
                            favoritos.product_id = v
                        try:
                            favoritos.save()
                        except IntegrityError:
                            raise Http404

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FavoritosApiView(APIView):

    def get_object(self, pk):
        try:
            return Produtos.objects.get(pk=pk)
        except Produtos.DoesNotExist:
            raise Http404
   
    def delete(self, request, pk, format=None):
        favorito = self.get_object(pk)
        favorito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)