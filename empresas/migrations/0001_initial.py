# Generated by Django 4.1.13 on 2024-03-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=255)),
                ('telCelular', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('telFixo', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone fixo')),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_update', models.DateTimeField(auto_now=True)),
                ('dt_enc', models.DateTimeField(blank=True, null=True)),
                ('cep', models.CharField(blank=True, max_length=10)),
                ('bairro', models.CharField(blank=True, max_length=255)),
                ('rua', models.CharField(blank=True, max_length=255)),
                ('complemento', models.CharField(blank=True, max_length=255)),
                ('numero', models.CharField(blank=True, max_length=10)),
                ('estado', models.CharField(blank=True, max_length=2)),
                ('cidade', models.CharField(blank=True, max_length=255)),
                ('cep2', models.CharField(blank=True, max_length=10)),
                ('bairro2', models.CharField(blank=True, max_length=255)),
                ('rua2', models.CharField(blank=True, max_length=255)),
                ('complemento2', models.CharField(blank=True, max_length=255)),
                ('numero2', models.CharField(blank=True, max_length=10)),
                ('estado2', models.CharField(blank=True, max_length=2)),
                ('cidade2', models.CharField(blank=True, max_length=255)),
                ('email2', models.EmailField(max_length=255)),
                ('telCelular2', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('telFixo2', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone fixo')),
            ],
        ),
    ]
