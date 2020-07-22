from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.clientes.models import Clientes
from apps.produtos.models import Produtos
from apps.favoritos.models import Favoritos


class ClientesSerializer(serializers.Serializer):
    # class Meta:
    #     model = Clientes
    #     fields = ('__all__')
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=254)
    cpf = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return Clientes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('validated_data', validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ('__all__')
        
        def create(self, validated_data):
            return Produtos.objects.create(**validated_data)

class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ('__all__')