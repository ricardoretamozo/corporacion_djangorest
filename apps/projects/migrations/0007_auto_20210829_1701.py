# Generated by Django 3.2.5 on 2021-08-29 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20210719_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalproductionorder',
            name='Cantidad',
        ),
        migrations.RemoveField(
            model_name='productionorder',
            name='Cantidad',
        ),
    ]