from rest_framework.routers import DefaultRouter
from apps.supplies.api.views import SuppliesViewSet

router = DefaultRouter()

router.register(r'supplies',SuppliesViewSet,basename = 'supplies')

urlpatterns = router.urls