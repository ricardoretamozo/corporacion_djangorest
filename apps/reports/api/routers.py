from rest_framework.routers import DefaultRouter
from apps.reports.api.views.reports_viewset import ReportsViewSet
from apps.reports.api.views.general_views import *

router = DefaultRouter()

router.register(r'reports',ReportsViewSet,basename = 'report')
router.register(r'materias',MaterialsViewSet,basename = 'materias')
router.register(r'tareo',TareoViewSet,basename = 'tareo')
router.register(r'endurancetest',EndurancetestViewSet,basename = 'endurancetest')
router.register(r'airforce',AirForceSerializerViewSet,basename = 'airforce')
router.register(r'servicerequirement',ServiceRequirementViewSet,basename = 'servicerequirement')
router.register(r'productservice',ProductServiceViewSet,basename = 'productservice')

urlpatterns = router.urls