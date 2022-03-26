from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class Business(BaseModel):

    Ruc = models.CharField('Ruc de empresa', max_length=12, blank= False , null = False, unique = True)
    name = models.CharField('Nombre ', max_length=50 , default='')
    DirecionFiscal = models.CharField('Direción fiscal',max_length=120)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name

class Campus(BaseModel):

    # TODO: Define fields here
    Direccion = models.CharField('Direccion de la planta', max_length=120,blank = False,null = False,unique = True)
    Business_Campus = models.ForeignKey(Business, on_delete=models.CASCADE,verbose_name = 'Indicador de Empresa',blank = False,null = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Direcion de la planta'
        verbose_name_plural = 'Direciones de la planta'

    def __str__(self):
        return self.Direccion