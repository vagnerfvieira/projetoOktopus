# Generated by Django 5.0.4 on 2024-05-15 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='titulo')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='preço')),
                ('manufacturing_date', models.DateField(blank=True, null=True, verbose_name='data de fabricação')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='data de vencimento')),
            ],
        ),
    ]
