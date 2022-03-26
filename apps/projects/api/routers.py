from rest_framework.routers import DefaultRouter
from apps.projects.api.views.projects_viewsets import ProjectsViewSet
from apps.projects.api.views.general_views import (
    ProjectsProductViewSet,MaterialOriginViewSet,MaterialsCementViewSet,MaterialsM3ViewSet,
    MaterialsPieceViewSet,QuadrilaDayViewSet,ReinforcementSteelViewSet,ProductionOrderViewSet)

router = DefaultRouter()

router.register(r'projects',ProjectsViewSet,basename = 'project')
router.register(r'productionorder',ProductionOrderViewSet,basename = 'productionorder')
router.register(r'projectsproduct',ProjectsProductViewSet,basename = 'projectsproduct')
router.register(r'materialorigin',MaterialOriginViewSet,basename = 'materialorigin')
router.register(r'materialcement',MaterialsCementViewSet,basename = 'materialcement')
router.register(r'materialsm3',MaterialsM3ViewSet,basename = 'materialsm3')
router.register(r'materialspiece',MaterialsPieceViewSet,basename = 'materialspiece')
router.register(r'quadriladay',QuadrilaDayViewSet,basename = 'quadriladay')
router.register(r'reinforcementsteel',ReinforcementSteelViewSet,basename = 'reinforcementsteel')
urlpatterns = router.urls