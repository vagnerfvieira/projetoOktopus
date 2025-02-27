# Generated by Django 4.1.13 on 2024-03-18 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoFinConta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeGrupoFin', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SubGrupoFinConta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeSubGrupoFinConta', models.CharField(max_length=25)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_update', models.DateTimeField(auto_now=True)),
                ('dt_enc', models.DateTimeField(blank=True, null=True)),
                ('grupoFin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subgrupo', to='contaFinanças.grupofinconta')),
            ],
        ),
        migrations.CreateModel(
            name='ContaFin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeContaFin', models.CharField(max_length=25)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_update', models.DateTimeField(auto_now=True)),
                ('dt_enc', models.DateTimeField(blank=True, null=True)),
                ('subGrupoContaFin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conta', to='contaFinanças.subgrupofinconta')),
            ],
        ),
    ]
