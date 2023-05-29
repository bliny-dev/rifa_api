from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class PrizeDraw(models.Model):
    name = models.CharField('Nome', max_length=200)
    descricao = models.TextField('Descrição', max_length=200)
    price = models.FloatField('Preço')
    qtd_prize_draw = models.IntegerField('Quantidade de sorteio')
    date_prize_draw = models.DateTimeField('Data do sorteio')
    status = models.BooleanField('status')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_sorteio = models.ImageField(upload_to="rifa_img/") 

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Sorteio'
        verbose_name_plural = 'Sorteios'


