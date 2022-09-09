# Generated by Django 4.1 on 2022-09-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=50)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
        ),
    ]