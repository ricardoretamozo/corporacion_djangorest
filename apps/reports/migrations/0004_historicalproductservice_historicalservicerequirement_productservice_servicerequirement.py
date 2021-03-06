# Generated by Django 3.2.5 on 2021-07-18 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0003_historicalsupplies'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0005_auto_20210718_0028'),
        ('reports', '0003_airforce_endurancetest_historicalairforce_historicalendurancetest'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequirement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('FechaEmision', models.DateField(verbose_name='Fecha emision')),
                ('Atencion', models.CharField(choices=[('Normal', 'NORMAL'), ('Urgente', 'URGENTE')], max_length=50, verbose_name='Atención')),
                ('Observacion', models.TextField(verbose_name='Observacion')),
                ('Order_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.productionorder', verbose_name='Orden producción')),
            ],
            options={
                'verbose_name': 'Requerimiento de compra y/o servicio',
                'verbose_name_plural': 'Requerimientos de compra y/o servicios',
            },
        ),
        migrations.CreateModel(
            name='ProductService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('FechaDelivery', models.DateField(verbose_name='Fecha entrega')),
                ('LugarEntrega', models.CharField(max_length=50, verbose_name='Lugar de entega')),
                ('Cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('ServiceRequirementProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.servicerequirement', verbose_name='Servicio requerimiento')),
                ('Supplie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.supplies', verbose_name='Insumos')),
            ],
            options={
                'verbose_name': 'Producto y/o servicio',
                'verbose_name_plural': 'Productos y/o servicios',
            },
        ),
        migrations.CreateModel(
            name='HistoricalServiceRequirement',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('FechaEmision', models.DateField(verbose_name='Fecha emision')),
                ('Atencion', models.CharField(choices=[('Normal', 'NORMAL'), ('Urgente', 'URGENTE')], max_length=50, verbose_name='Atención')),
                ('Observacion', models.TextField(verbose_name='Observacion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Order_Product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.productionorder', verbose_name='Orden producción')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Requerimiento de compra y/o servicio',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProductService',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('FechaDelivery', models.DateField(verbose_name='Fecha entrega')),
                ('LugarEntrega', models.CharField(max_length=50, verbose_name='Lugar de entega')),
                ('Cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('ServiceRequirementProduct', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='reports.servicerequirement', verbose_name='Servicio requerimiento')),
                ('Supplie', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='supplies.supplies', verbose_name='Insumos')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Producto y/o servicio',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
