from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.business.models import Business
# Create your models here.

class Client(BaseModel):

    Razon_Social = models.CharField('Razon Social', max_length=100)
    Direccion_Fiscal = models.CharField('Dirección Fiscal', max_length=150)
    DNI_RUC = models.CharField('dni o ruc', max_length=11 , unique =True,blank = False,null = False)
    Persona_Nombre = models.CharField('Nombres', max_length=150)
    Persona_Telefono = models.CharField('Telefono', max_length=150)
    Persona_Correo = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    Business_Client = models.ForeignKey(Business, on_delete=models.CASCADE,verbose_name = 'Empresa',blank = False,null = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.Persona_Nombre