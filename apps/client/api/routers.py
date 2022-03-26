from rest_framework.routers import DefaultRouter
from apps.client.api.views import ClientViewSet

router = DefaultRouter()

router.register(r'client',ClientViewSet,basename = 'client')

urlpatterns = router.urls