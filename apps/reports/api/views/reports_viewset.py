from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.users.authentication_mixins import Authentication
from apps.reports.api.serializers.reports_serializers import ReportsSerializer

class ReportsViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ReportsSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Reporte eliminado correctamente!'},status = status.HTTP_200_OK)
        return Response({'error':'No existe un Reporte con estos datos!'},status = status.HTTP_400_BAD_REQUEST)