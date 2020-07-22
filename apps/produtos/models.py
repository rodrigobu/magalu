from django.db import models

class Produtos(models.Model):
    price = models.DecimalField(verbose_name='Preço', max_digits=6, decimal_places=2)
    image = models.URLField(verbose_name='Url da Imagem do Produto', blank=True )
    brand = models.CharField(verbose_name='Marca do Produto', max_length=254)
    title = models.CharField(verbose_name='Titulo', max_length=254)
    review_score = models.IntegerField(verbose_name='Review do Produto', default=0 )

    def __str__(self):
        return "{} - {}".format(self.title, self.price) 