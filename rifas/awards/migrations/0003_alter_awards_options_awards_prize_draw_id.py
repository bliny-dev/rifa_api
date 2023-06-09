# Generated by Django 4.2.1 on 2023-05-29 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prize_draw', '0003_alter_prizedraw_options_remove_prizedraw_awards'),
        ('awards', '0002_remove_awards_descricao_premio_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='awards',
            options={'verbose_name': 'Premio', 'verbose_name_plural': 'Premios'},
        ),
        migrations.AddField(
            model_name='awards',
            name='prize_draw_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prize_draw.prizedraw', verbose_name='ID do sorteio'),
        ),
    ]
