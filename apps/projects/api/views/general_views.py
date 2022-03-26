from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from apps.base.api import GeneralListApiView
from apps.users.authentication_mixins import Authentication
from apps.projects.api.serializers.general_serializers import (
    ProjectsProductSerializer,MaterialOriginSerializer,MaterialsCementSerializer,MaterialsM3Serializer,
    MaterialsPieceSerializer,QuadrilaDaySerializer,ReinforcementSteelSerializer,ProductionOrderSerializer)

class ProjectsProductViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ProjectsProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Project']
    def get_queryset(self,pk=None):
        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(Project = pk,state = True).first()


    def destroy(self,request,pk=None):
        product = self.get_queryset().filter(id = pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente del proyecto!'},status = status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos en un proycto!'},status = status.HTTP_400_BAD_REQUEST)

class MaterialOriginViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = MaterialOriginSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Order_Product']
    
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

class MaterialsCementViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = MaterialsCementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Order_Product']
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

class MaterialsM3ViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = MaterialsM3Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Order_Product']
    
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

class MaterialsPieceViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = MaterialsPieceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Order_Product']
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

class QuadrilaDayViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = QuadrilaDaySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Order_Product']

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

class ReinforcementSteelViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ReinforcementSteelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Order_Product']

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

class ProductionOrderViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ProductionOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Projects_Product']

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
