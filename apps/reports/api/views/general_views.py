from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.users.authentication_mixins import Authentication
from apps.reports.api.serializers.general_serializers import *


class MaterialsViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = MaterialsSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Eliminado correctamente del proyecto!'},status = status.HTTP_200_OK)
        return Response({'error':'No existe estos datos!'},status = status.HTTP_400_BAD_REQUEST)

class TareoViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = TareoSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Eliminado correctamente del proyecto!'},status = status.HTTP_200_OK)
        return Response({'error':'No existe estos datos!'},status = status.HTTP_400_BAD_REQUEST)

class EndurancetestViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = EndurancetestSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Eliminado correctamente del proyecto!'},status = status.HTTP_200_OK)
        return Response({'error':'No existe estos datos!'},status = status.HTTP_400_BAD_REQUEST)

class AirForceSerializerViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = AirForceSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Eliminado correctamente del proyecto!'},status = status.HTTP_200_OK)
        return Response({'error':'No existe estos datos!'},status = status.HTTP_400_BAD_REQUEST)

class ServiceRequirementViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ServiceRequirementSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Eliminado correctamente del proyecto!'},status = status.HTTP_200_OK)
        return Response({'error':'No existe estos datos!'},status = status.HTTP_400_BAD_REQUEST)

class ProductServiceViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ProductServiceSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Eliminado correctamente del proyecto!'},status = status.HTTP_200_OK)
        return Response({'error':'No existe estos datos!'},status = status.HTTP_400_BAD_REQUEST)
