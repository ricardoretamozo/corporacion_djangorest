from django.contrib import admin
from apps.projects.models import Projects
from apps.projects.models import ProjectsProduct,QuadrilaDay,ReinforcementSteel
from apps.projects.models import ProductionOrder,MaterialOrigin,MaterialsCement,MaterialsM3,MaterialsPiece
admin.site.register(Projects)
admin.site.register(ProjectsProduct)
admin.site.register(ProductionOrder)
admin.site.register(MaterialOrigin)
admin.site.register(MaterialsCement)
admin.site.register(MaterialsM3)
admin.site.register(MaterialsPiece)
admin.site.register(QuadrilaDay)
admin.site.register(ReinforcementSteel)
# Register your models here.
