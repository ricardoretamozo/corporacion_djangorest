# Generated by Django 3.2.5 on 2021-07-17 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('DNI', models.CharField(max_length=8, unique=True, verbose_name='DNI Trabajador')),
                ('name', models.CharField(max_length=50, verbose_name='Nombres ')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellidos ')),
                ('Rol', models.CharField(choices=[('Ayudante', 'Ayudante de planta'), ('Ingeniero', 'Ingeniero')], max_length=50, verbose_name='Rol')),
                ('Business_Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business', verbose_name='Trabajar de..')),
            ],
            options={
                'verbose_name': 'Trabador',
                'verbose_name_plural': 'Trabajadores',
            },
        ),
    ]
