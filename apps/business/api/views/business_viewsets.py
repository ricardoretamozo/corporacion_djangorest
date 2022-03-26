from apps.base.api import GeneralListApiView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from apps.users.authentication_mixins import Authentication
from apps.business.api.serializers.business_serializers import BusinessSerializer


class BusinessViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = BusinessSerializer
    #queryset = BusinessSerializer.Meta.model.objects.filter(state = True)
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk , state = True).first()

    def create(self,request):
        serializer = self.serializer_class(data  =request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Empresa creada correctamente!'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            business_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if business_serializer.is_valid():
                business_serializer.save()
                return Response(business_serializer.data, status = status.HTTP_200_OK)
            return Response(business_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def destroy(self, request , pk=None):
        business =self.get_queryset().filter(id = pk).first()

        if business:
            business.state = False
            business.save()
            return Response({'message':'Empresa eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un empresa con esos datos!'}, status = status.HTTP_400_BAD_REQUEST)



"""
class BusinessCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BusinessSerializer
    queryset = BusinessSerializer.Meta.model.objects.filter(state = True)

    def post(self,request):
        serializer = self.serializer_class(data  =request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Empresa creada correctamente!'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class BusinessRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BusinessSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk , state = True).first()

    def patch(self,request,pk=None):
        business = self.get_queryset(pk)
        if business:
            business_serializer = self.serializer_class(business)
            return Response(business_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'No existe un empresa con esos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            business_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if business_serializer.is_valid():
                business_serializer.save()
                return Response(business_serializer.data, status = status.HTTP_200_OK)
            return Response(business_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request , pk=None):
        business =self.get_queryset().filter(id = pk).first()

        if business:
            business.state = Fasle
            business.save()
            return Response({'message':'Empresa eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un empresa con esos datos!'}, status = status.HTTP_400_BAD_REQUEST)



class BusinessRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BusinessSerializer

    def get_queryset(self):
        return super().get_serializer().Meta.model.objects.filter(state = True)

    
    
class BusinessDestroyAPIView(generics.DestroyAPIView):
    serializer_class = BusinessSerializer

    def get_queryset(self):
        return super().get_serializer().Meta.model.objects.filter(state = True)

    def delete(self, request , pk=None):
        business =self.get_queryset().filter(id = pk).first()

        if business:
            business.state = Fasle
            business.save()
            return Response({'message':'Empresa eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un empresa con esos datos!'}, status = status.HTTP_400_BAD_REQUEST)


class BusinessUpdateAPIView(generics.UpdateAPIView):
    serializer_class = BusinessSerializer

    def get_queryset(self,pk):
        return super().get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    def patch(self,request,pk=None):
        business = self.get_queryset(pk)
        if business:
            business_serializer = self.serializer_class(business)
            return Response(business_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'No existe un empresa con esos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            business_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if business_serializer.is_valid():
                business_serializer.save()
                return Response(business_serializer.data, status = status.HTTP_200_OK)
            return Response(business_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

"""