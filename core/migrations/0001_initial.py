# Generated by Django 4.2.11 on 2024-04-05 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criando em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
            ],
        ),
    ]
