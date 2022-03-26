from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.business.models import Business

# Create your models here.

class Products(BaseModel):

    Business_Products = models.ForeignKey(Business, on_delete=models.CASCADE,verbose_name = 'Empresa',blank = False,null = False)
    name = models.CharField('Nombre de producto', max_length=100)
    plano = models.FileField('PDF Plano o Ficha Tecnica', upload_to="productos/plano/%c/pdf",blank = True,null = True ,default = "doc.pdf")
    expediente_diseno = models.FileField('PDF Expediente diseño', upload_to="productos/expediente_diseno/%c/pdf", blank = True,null = True,default = "doc.pdf")
    plano_molde = models.FileField('PDF Plano de molde', upload_to="productos/plano_molde/%c/pdf", blank = True,null = True,default = "doc.pdf")
    Costo_Produccion = models.IntegerField('Costo produción')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name