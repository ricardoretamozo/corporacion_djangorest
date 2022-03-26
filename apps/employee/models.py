from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
from apps.business.models import Business
# Create your models here.

class Employee(BaseModel):

    Type_of_roles = (
        ('Ayudante', 'Ayudante de planta'),
        ('Ingeniero', 'Ingeniero'),
    )
    
    DNI = models.CharField('DNI Trabajador', max_length=8 , unique=True ,blank = False,null = False)
    Business_Employee = models.ForeignKey(Business, on_delete=models.CASCADE,verbose_name = 'Empresa',blank = False,null = False)
    name = models.CharField('Nombres ', max_length=50)
    last_name = models.CharField('Apellidos ', max_length=50)
    Rol = models.CharField('Rol' ,max_length=50 , choices=Type_of_roles)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Trabador'
        verbose_name_plural = 'Trabajadores'

    def __str__(self):
        return self.name


