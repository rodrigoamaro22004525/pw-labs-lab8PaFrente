# Generated by Django 4.0.5 on 2022-06-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_projetos_linha'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='gitLink',
            field=models.CharField(default='https://github.com/rodrigoamaro22004525', max_length=200),
        ),
    ]
