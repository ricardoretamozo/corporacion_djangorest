from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.projects.models import ProductionOrder
from apps.supplies.models import Supplies
from apps.employee.models import Employee

# Create your models here.

class Reports(BaseModel):

    Order_Product = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE,verbose_name = 'Orden producción',blank = False,null = False)
    FechaProduccion = models.DateField('Fecha Produccion', auto_now=False, auto_now_add=False)
    Cantidad = models.IntegerField('Cantidad de productos')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'

    def __str__(self):
        return self.Order_Product

class Materials(BaseModel):

    Report_Materials = models.ForeignKey(Reports, on_delete=models.CASCADE,verbose_name = 'Reporte',blank = False,null = False)
    Supplie = models.ForeignKey(Supplies, on_delete=models.CASCADE,verbose_name = 'Insumos',blank = False,null = False)
    Cantidad = models.IntegerField('Cantidad de insumos')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Materila utilizado'
        verbose_name_plural = 'Materiales utilizados'

    def __str__(self):
        return self.Report_Materials

class Tareo(BaseModel):

    Report_Materials = models.ForeignKey(Reports, on_delete=models.CASCADE,verbose_name = 'Reporte',blank = False,null = False)
    Tareo_Employee = models.ForeignKey(Employee, on_delete=models.CASCADE,verbose_name = 'Trabajadores',blank = False,null = False)
    HoursEntry = models.TimeField('Hora de ingreso', auto_now=False, auto_now_add=False)
    HoursExit = models.TimeField('Hora de salida' ,auto_now=False, auto_now_add=False)
    Refreshment = models.TimeField('Min de refiregerio', auto_now=False, auto_now_add=False)
    HoursJob = models.TimeField('Horas trasncurridas', auto_now=False, auto_now_add=False)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Control Asistencia'
        verbose_name_plural = 'Controles de asistencia'

    def __str__(self):
        return self.Report_Materials

class Endurancetest(BaseModel):

    Report_Materials = models.ForeignKey(Reports, on_delete=models.CASCADE,verbose_name = 'Reporte',blank = False,null = False)
    FechaVaciado = models.DateField('Fecha vaciado', auto_now=False, auto_now_add=False)
    FechaRotura = models.DateField('Fecha rotura', auto_now=False, auto_now_add=False)
    PromedioFc = models.DecimalField('Promedio Fc (KgF/cm2)', max_digits=5, decimal_places=2)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Ensayo de resistencia'
        verbose_name_plural = 'Ensayos de resistencias'

    def __str__(self):
        return self.Report_Materials

class AirForce(BaseModel):

    AirForceEndurancetest = models.ForeignKey(Endurancetest, on_delete=models.CASCADE,verbose_name = 'Ensayo de resistencia',blank = False,null = False)
    ForceCompressionKn = models.DecimalField('Fuerza de compresion (Kn)', max_digits=5, decimal_places=2)
    AirCompressionCm2 = models.DecimalField('Area de compresion (cm2)', max_digits=5, decimal_places=2)
    ForceCompressionKgF = models.DecimalField('Fuerza de compresion (KgF)', max_digits=5, decimal_places=2)
    Endurance = models.DecimalField('Resistencia (KgF/cm2)', max_digits=5, decimal_places=2)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Fuerza y Area'
        verbose_name_plural = 'Fuerzas y Areas'

    def __str__(self):
        return self.AirForceEndurancetest

#REQUERIMIENTO DE COMPRA Y/O SERVICIO
class ServiceRequirement(BaseModel):

    Type = (
        ('Normal', 'NORMAL'),
        ('Urgente', 'URGENTE'),
    )

    Order_Product = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE,verbose_name = 'Orden producción',blank = False,null = False)
    FechaEmision = models.DateField('Fecha emision', auto_now=False, auto_now_add=False)
    Atencion = models.CharField('Atención', choices=Type, max_length=50 )
    Observacion = models.TextField('Observacion')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Requerimiento de compra y/o servicio'
        verbose_name_plural = 'Requerimientos de compra y/o servicios'

    def __str__(self):
        return self.Order_Product

class ProductService(BaseModel):

    ServiceRequirementProduct = models.ForeignKey(ServiceRequirement, on_delete=models.CASCADE,verbose_name = 'Servicio requerimiento',blank = False,null = False)
    Supplie = models.ForeignKey(Supplies, on_delete=models.CASCADE,verbose_name = 'Insumos',blank = False,null = False)
    FechaDelivery = models.DateField('Fecha entrega', auto_now=False, auto_now_add=False)
    LugarEntrega = models.CharField('Lugar de entega', max_length=50)
    Cantidad = models.IntegerField('Cantidad')
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto y/o servicio'
        verbose_name_plural = 'Productos y/o servicios'

    def __str__(self):
        return self.ServiceRequirementProduct