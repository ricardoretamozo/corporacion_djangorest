# Generated by Django 3.2.5 on 2021-07-17 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20210717_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproductionorder',
            name='Projects_Product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.projectsproduct', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='productionorder',
            name='Projects_Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectsproduct', verbose_name='Producto'),
        ),
        migrations.CreateModel(
            name='MaterialsPiece',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('AgregadoGrueso', models.IntegerField(verbose_name='Agregado grueso(kg)')),
                ('AgregadoFino', models.IntegerField(verbose_name='Agregado fino(kg)')),
                ('Cemento', models.IntegerField(verbose_name='Cemento(kg)')),
                ('Aditivo', models.IntegerField(verbose_name='Aditivo(kg)')),
                ('Agua', models.IntegerField(verbose_name='Agua(kg)')),
                ('Order_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.productionorder', verbose_name='Orden producción')),
            ],
            options={
                'verbose_name': 'Asignación de materiales  por pieza',
                'verbose_name_plural': 'Asignaciónes de materiales  por pieza',
            },
        ),
        migrations.CreateModel(
            name='MaterialsM3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('AgregadoGrueso', models.IntegerField(verbose_name='Agregado grueso(kg)')),
                ('AgregadoFino', models.IntegerField(verbose_name='Agregado fino(kg)')),
                ('Cemento', models.IntegerField(verbose_name='Cemento(kg)')),
                ('Aditivo', models.IntegerField(verbose_name='Aditivo(kg)')),
                ('Agua', models.IntegerField(verbose_name='Agua(kg)')),
                ('Order_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.productionorder', verbose_name='Orden producción')),
            ],
            options={
                'verbose_name': 'Asignación de materiales  por m3',
                'verbose_name_plural': 'Asignaciónes de materiales  por m3',
            },
        ),
        migrations.CreateModel(
            name='MaterialsCement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('AgregadoGrueso', models.IntegerField(verbose_name='Agregado grueso(kg)')),
                ('AgregadoFino', models.IntegerField(verbose_name='Agregado fino(kg)')),
                ('Cemento', models.IntegerField(verbose_name='Cemento(kg)')),
                ('Aditivo', models.IntegerField(verbose_name='Aditivo(kg)')),
                ('Agua', models.IntegerField(verbose_name='Agua(kg)')),
                ('Order_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.productionorder', verbose_name='Orden producción')),
            ],
            options={
                'verbose_name': 'Asignación de materiales  por bolsa cemento',
                'verbose_name_plural': 'Asignaciónes de materiales  por bolsa cemento',
            },
        ),
        migrations.CreateModel(
            name='MaterialOrigin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('ProcedenciaAgregadoGrueso', models.CharField(max_length=150, verbose_name='Procedencia agregado grueso')),
                ('ProcedenciaAgregadoFino', models.CharField(max_length=150, verbose_name='Procedencia agregado fino')),
                ('TipoCemento', models.CharField(max_length=150, verbose_name='Tipo de cemento')),
                ('TipoAditivo', models.CharField(max_length=150, verbose_name='Tipo de aditivo')),
                ('Order_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.productionorder', verbose_name='Orden producción')),
            ],
            options={
                'verbose_name': 'Procedencia del material',
                'verbose_name_plural': 'Procedencias de los materiales',
            },
        ),
        migrations.CreateModel(
            name='HistoricalMaterialsPiece',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('AgregadoGrueso', models.IntegerField(verbose_name='Agregado grueso(kg)')),
                ('AgregadoFino', models.IntegerField(verbose_name='Agregado fino(kg)')),
                ('Cemento', models.IntegerField(verbose_name='Cemento(kg)')),
                ('Aditivo', models.IntegerField(verbose_name='Aditivo(kg)')),
                ('Agua', models.IntegerField(verbose_name='Agua(kg)')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Order_Product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.productionorder', verbose_name='Orden producción')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Asignación de materiales  por pieza',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMaterialsM3',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('AgregadoGrueso', models.IntegerField(verbose_name='Agregado grueso(kg)')),
                ('AgregadoFino', models.IntegerField(verbose_name='Agregado fino(kg)')),
                ('Cemento', models.IntegerField(verbose_name='Cemento(kg)')),
                ('Aditivo', models.IntegerField(verbose_name='Aditivo(kg)')),
                ('Agua', models.IntegerField(verbose_name='Agua(kg)')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Order_Product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.productionorder', verbose_name='Orden producción')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Asignación de materiales  por m3',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMaterialsCement',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('AgregadoGrueso', models.IntegerField(verbose_name='Agregado grueso(kg)')),
                ('AgregadoFino', models.IntegerField(verbose_name='Agregado fino(kg)')),
                ('Cemento', models.IntegerField(verbose_name='Cemento(kg)')),
                ('Aditivo', models.IntegerField(verbose_name='Aditivo(kg)')),
                ('Agua', models.IntegerField(verbose_name='Agua(kg)')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Order_Product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.productionorder', verbose_name='Orden producción')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Asignación de materiales  por bolsa cemento',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMaterialOrigin',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('ProcedenciaAgregadoGrueso', models.CharField(max_length=150, verbose_name='Procedencia agregado grueso')),
                ('ProcedenciaAgregadoFino', models.CharField(max_length=150, verbose_name='Procedencia agregado fino')),
                ('TipoCemento', models.CharField(max_length=150, verbose_name='Tipo de cemento')),
                ('TipoAditivo', models.CharField(max_length=150, verbose_name='Tipo de aditivo')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('Order_Product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.productionorder', verbose_name='Orden producción')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Procedencia del material',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]