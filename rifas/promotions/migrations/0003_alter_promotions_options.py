# Generated by Django 4.2.1 on 2023-05-29 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_remove_promotions_preco_cotas_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promotions',
            options={'verbose_name': 'Cota', 'verbose_name_plural': 'Cotas'},
        ),
    ]
