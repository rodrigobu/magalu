from django.db import models

from apps.clientes.models import Clientes
from apps.produtos.models import Produtos

class Favoritos(models.Model):
    client = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    product = models.ForeignKey(Produtos, on_delete=models.CASCADE)



    def __str__(self):
        return '{} - {}'.format(self.client.name, self.product.title)