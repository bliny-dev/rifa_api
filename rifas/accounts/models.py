from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.
class User(AbstractUser):

    full_name = models.CharField('Nome completo', max_length=150)
    email = models.EmailField('Email', max_length=150)

def __str__(self):
    return str(self.id)

class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)