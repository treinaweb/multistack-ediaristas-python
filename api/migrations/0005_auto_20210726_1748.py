# Generated by Django 3.2.5 on 2021-07-26 17:48

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210726_1733'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome_completo',
            field=models.CharField(max_length=255, null=True),
        ),
    ]