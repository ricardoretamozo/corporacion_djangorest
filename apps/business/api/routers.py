from rest_framework.routers import DefaultRouter
from apps.business.api.views.business_viewsets import BusinessViewSet

router = DefaultRouter()

router.register(r'business',BusinessViewSet,basename = 'business')

urlpatterns = router.urls