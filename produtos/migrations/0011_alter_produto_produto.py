# Generated by Django 5.0.4 on 2024-05-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0010_alter_produto_estoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='produto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
