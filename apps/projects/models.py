from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel,MaterialsAllocation
from apps.business.models import Business
from apps.client.models import Client
from apps.products.models import Products
from apps.users.models import User
# Create your models here.

class Projects(BaseModel):

    Business_Projects = models.ForeignKey(Business, on_delete=models.CASCADE,verbose_name = 'Empresa',blank = False,null = False)
    Client_Projects = models.ForeignKey(Client, on_delete=models.CASCADE,verbose_name = 'Cliente',blank = False,null = False)
    name = models.CharField('Nombre', max_length=100)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.name

class ProjectsProduct(BaseModel):

    Project = models.ForeignKey(Projects, on_delete=models.CASCADE,verbose_name = 'Proyecto',blank = False,null = False)
    Product_Projects = models.ForeignKey(Products, on_delete=models.CASCADE,verbose_name = 'Producto',blank = False,null = False)
    Cantidad = models.IntegerField('Nro de productos')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Producto del proyecto'
        verbose_name_plural = 'Productos del proyecto'

    def __str__(self):
        return str(self.Product_Projects.name)

class ProductionOrder(BaseModel):

    attendant = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'Encargado',blank = False,null = False)
    Projects_Product = models.ForeignKey(ProjectsProduct, on_delete=models.CASCADE,verbose_name = 'Producto',blank = False,null = False)
    #Cantidad = models.IntegerField('Nro de productos especificos')
    date_final = models.DateField('Fecha Final', auto_now=False, auto_now_add=False)
    RatioProducción = models.IntegerField('Avanze de productos por dia')
    NroMoldes = models.IntegerField('Nro Moldes')
    Observacion = models.TextField('Observacciónes')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Órden de producción'
        verbose_name_plural = 'Órdenes de producción'

    def __str__(self):
        return self.Projects_Product.Project.name

class MaterialOrigin(BaseModel):

    Order_Product = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE,verbose_name = 'Orden producción',blank = False,null = False)
    ProcedenciaAgregadoGrueso = models.CharField('Procedencia agregado grueso', max_length=150)
    ProcedenciaAgregadoFino = models.CharField('Procedencia agregado fino', max_length=150)
    TipoCemento = models.CharField('Tipo de cemento', max_length=150)
    TipoAditivo = models.CharField('Tipo de aditivo', max_length=150)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Procedencia del material'
        verbose_name_plural = 'Procedencias de los materiales'

    def __str__(self):
        return self.Order_Product.Projects_Product.Project.name

#allocation of materials by cement bag
class MaterialsCement(MaterialsAllocation):

    Order_Product = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE,verbose_name = 'Orden producción',blank = False,null = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Asignación de materiales  por bolsa cemento'
        verbose_name_plural = 'Asignaciónes de materiales  por bolsa cemento'

    def __str__(self):
        return self.Order_Product.Projects_Product.Project.name

#allocation of materials per m3
class MaterialsM3(MaterialsAllocation):

    Order_Product = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE,verbose_name = 'Orden producción',blank = False,null = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Asignación de materiales  por m3'
        verbose_name_plural = 'Asignaciónes de materiales  por m3'

    def __str__(self):
        return self.Order_Product.Projects_Product.Project.name

#allocation of materials by piece
class MaterialsPiece(MaterialsAllocation):

    Order_Product = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE,verbose_name = 'Orden producción',blank = False,null = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Asignación de materiales  por pieza'
        verbose_name_plural = 'Asignaciónes de materiales  por pieza'

    def __str__(self):
        return self.Order_Product.Projects_Product.Project.name

class QuadrilaDay(BaseModel):

    Order_Product = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE,verbose_name = 'Orden producción',blank = False,null = False)
    NroOperarios = models.IntegerField('Nro de operarios')
    NroAyudante = models.IntegerField('Nro de ayudantes')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Asignación de cuadrilla/jornada'
        verbose_name_plural = 'Asignaciónes de cuadrilla/jornada'

    def __str__(self):
        return self.Order_Product.Projects_Product.Project.name

class ReinforcementSteel(BaseModel):

    
    Type_of_varilla = (
        
    )

    Order_Product = models.ForeignKey(ProductionOrder, on_delete=models.CASCADE,verbose_name = 'Orden producción',blank = False,null = False)
    TipoVarilla = models.CharField('Tipo de varilla', max_length=50)
    CantidadVarilla = models.IntegerField('Cantidad de varilla(m)')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Asignación de acero refuerzo'
        verbose_name_plural = 'Asignaciónes de acero refuerzo'

    def __str__(self):
        return self.TipoVarilla

