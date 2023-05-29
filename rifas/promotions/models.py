from django.db import models

from prize_draw.models import PrizeDraw

# Create your models here.
class Promotions(models.Model):
    qtd_quotas = models.IntegerField('Quantidade da cotas', null=True)
    price_quotas = models.FloatField('Preço das cotas', null=True) 
    prize_draw = models.ForeignKey(PrizeDraw, verbose_name="Sorteio", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.prize_draw 

    class Meta:
        verbose_name = 'Cota'
        verbose_name_plural = 'Cotas'