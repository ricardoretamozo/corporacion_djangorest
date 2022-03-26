from apps.base.api import GeneralListApiView
from apps.business.api.serializers.general_serializers import CampusSerializer
from apps.users.authentication_mixins import Authentication
class CampusUnitListAPIView(Authentication,GeneralListApiView):
    serializer_class = CampusSerializer


