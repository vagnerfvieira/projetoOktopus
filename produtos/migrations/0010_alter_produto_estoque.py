# Generated by Django 5.0.4 on 2024-05-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_alter_produto_estoque_minimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
