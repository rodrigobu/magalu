# Generated by Django 3.0.8 on 2020-07-22 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('address', models.CharField(max_length=100, verbose_name='Endereço')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
            ],
        ),
    ]
