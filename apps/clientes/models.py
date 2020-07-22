from django.db import models


class Clientes(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=30, blank=False)
    cpf = models.CharField(verbose_name="CPF",max_length=15)
    address = models.CharField(verbose_name="Endereço", max_length=100)
    email = models.EmailField(verbose_name="E-mail", max_length=254, unique=True)

    def __str__(self):
        return self.name
