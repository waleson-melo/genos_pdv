# Generated by Django 4.1 on 2022-09-12 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, max_length=100, null=True)),
                ('estoque', models.IntegerField()),
                ('valor', models.FloatField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produtos.categoria')),
            ],
        ),
    ]
