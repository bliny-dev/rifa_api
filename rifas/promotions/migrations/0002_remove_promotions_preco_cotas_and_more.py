# Generated by Django 4.2.1 on 2023-05-29 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotions',
            name='preco_cotas',
        ),
        migrations.RemoveField(
            model_name='promotions',
            name='qtd_cotas',
        ),
        migrations.AddField(
            model_name='promotions',
            name='price_quotas',
            field=models.FloatField(null=True, verbose_name='Preço das cotas'),
        ),
        migrations.AddField(
            model_name='promotions',
            name='qtd_quotas',
            field=models.IntegerField(null=True, verbose_name='Quantidade da cotas'),
        ),
    ]