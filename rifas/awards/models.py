from django.db import models

from prize_draw.models import PrizeDraw
# Create your models here.
class Awards(models.Model):
    prize_number = models.IntegerField('Número do premio', null=True)
    description_prize = models.CharField('Descrição do premio',max_length=50, null=True)
    prize_draw_id = models.ForeignKey(PrizeDraw, verbose_name="ID do sorteio", null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.prize_number 

    class Meta:
        verbose_name = 'Premio'
        verbose_name_plural = 'Premios'