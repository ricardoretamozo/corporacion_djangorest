from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.users.authentication_mixins import Authentication
from apps.client.api.serializers import ClientSerializer

class ClientViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def list(self,request):
        #print(self.user)
        client_serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(client_serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        # send information to serializer
        serializer = self.serializer_class(data = request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Cliente creado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            client_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)            
            if client_serializer.is_valid():
                client_serializer.save()
                return Response(client_serializer.data,status = status.HTTP_200_OK)
            return Response(client_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        client = self.get_queryset().filter(id = pk).first() # get instance        
        if client:
            client.state = False
            client.save()
            return Response({'message':'Cliente eliminado correctamente!'},status = status.HTTP_200_OK)
        return Response({'error':'No existe un Cliente con estos datos!'},status = status.HTTP_400_BAD_REQUEST)