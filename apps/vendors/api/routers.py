from rest_framework.routers import DefaultRouter
from apps.vendors.api.views import VendorsViewSet

router = DefaultRouter()

router.register(r'vendors',VendorsViewSet,basename = 'vendors')

urlpatterns = router.urls