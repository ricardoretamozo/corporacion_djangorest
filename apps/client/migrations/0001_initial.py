# Generated by Django 3.2.5 on 2021-07-17 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0002_auto_20210717_0331'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalClient',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('Razon_Social', models.CharField(max_length=100, verbose_name='Razon Social')),
                ('Direccion_Fiscal', models.CharField(max_length=150, verbose_name='Dirección Fiscal')),
                ('DNI_RUC', models.CharField(db_index=True, max_length=11, verbose_name='dni o ruc')),
                ('Persona_Nombre', models.CharField(max_length=150, verbose_name='Nombres')),
                ('Persona_Telefono', models.CharField(max_length=150, verbose_name='Telefono')),
                ('Persona_Correo', models.EmailField(db_index=True, max_length=255, verbose_name='Correo Electrónico')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Business_Client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='business.business', verbose_name='Empresa')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Cliente',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('Razon_Social', models.CharField(max_length=100, verbose_name='Razon Social')),
                ('Direccion_Fiscal', models.CharField(max_length=150, verbose_name='Dirección Fiscal')),
                ('DNI_RUC', models.CharField(max_length=11, unique=True, verbose_name='dni o ruc')),
                ('Persona_Nombre', models.CharField(max_length=150, verbose_name='Nombres')),
                ('Persona_Telefono', models.CharField(max_length=150, verbose_name='Telefono')),
                ('Persona_Correo', models.EmailField(max_length=255, unique=True, verbose_name='Correo Electrónico')),
                ('Business_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.business', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
