# Generated by Django 4.0.5 on 2022-06-17 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_tecnologias_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projetos',
            old_name='imagem',
            new_name='img',
        ),
    ]
