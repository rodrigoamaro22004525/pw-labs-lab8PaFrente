# Generated by Django 4.0.4 on 2022-06-04 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_pontuacaoquizz_user_alter_pontuacaoquizz_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontuacaoquizz',
            name='user',
        ),
    ]
