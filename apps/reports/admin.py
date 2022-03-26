from django.contrib import admin
from apps.reports.models import Reports,Materials,Tareo,Endurancetest,AirForce,ServiceRequirement,ProductService

admin.site.register(Reports)
admin.site.register(Materials)
admin.site.register(Tareo)
admin.site.register(Endurancetest)
admin.site.register(AirForce)
admin.site.register(ServiceRequirement)
admin.site.register(ProductService)
# Register your models here.
