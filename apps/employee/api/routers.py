from rest_framework.routers import DefaultRouter
from apps.employee.api.views import EmpleyeeViewSet

router = DefaultRouter()

router.register(r'employee',EmpleyeeViewSet,basename = 'employee')

urlpatterns = router.urls