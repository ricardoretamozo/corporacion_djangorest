# Generated by Django 3.2.5 on 2021-07-23 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_historicalproducts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalproducts',
            old_name='Costo_Producción',
            new_name='Costo_Produccion',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='Costo_Producción',
            new_name='Costo_Produccion',
        ),
    ]