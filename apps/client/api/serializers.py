from rest_framework import serializers

from apps.client.models import Client

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'Razon_Social': instance.Razon_Social,
            'Direccion_Fiscal': instance.Direccion_Fiscal,
            'DNI_RUC': instance.DNI_RUC,
            'Persona_Telefono':instance.Persona_Telefono,
            'Persona_Nombre': instance.Persona_Nombre,
            'Persona_Correo': instance.Persona_Correo,
            'Business_Client': instance.Business_Client.name if instance.Business_Client is not None else ''
        }