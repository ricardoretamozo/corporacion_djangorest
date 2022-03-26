from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.business.models import Business
from apps.vendors.models import Vendors
# Create your models here.

class Supplies(BaseModel):

    Unit_of_measurement = (
        ('Bolsas', 'bolsas'),
        ('Unidad', 'Unid'),
        ('IBC ', 'IBC'),
        ('Glb', 'Glb'),
        ('Kilo gramos', 'Kg'),
        ('Gramos', 'g'),
        ('Baldes', 'baldes'),
    )

    Business_Supplies = models.ForeignKey(Business, on_delete=models.CASCADE,verbose_name = 'Empresa',blank = False,null = False)
    name = models.CharField('Nombre de insumo ', max_length=50)
    marca = models.CharField('Marca ', max_length=50)
    description = models.TextField('Descripcion del insumo')
    UnitOfMeasurement = models.CharField('Unidad de medida', max_length=50 , choices=Unit_of_measurement)
    Vendors_Supplies = models.ForeignKey(Vendors, on_delete=models.CASCADE,verbose_name = 'Proveedor',blank = False,null = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

    def __str__(self):
        return self.name
