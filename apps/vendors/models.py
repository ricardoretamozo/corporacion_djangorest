from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.

class Vendors(BaseModel):

    name = models.CharField('Nombre del proveedor ', max_length=50)
    phone = models.CharField('Telefono ', max_length=50)
    correo = models.EmailField('Correo', max_length=254)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.name