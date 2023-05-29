from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):

    full_name = models.CharField('Nome completo', max_length=150)
    email = models.EmailField('Email', max_length=150)

class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'