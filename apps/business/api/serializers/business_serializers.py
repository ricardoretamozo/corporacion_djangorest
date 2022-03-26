from rest_framework import serializers

from apps.business.models import Business

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'Ruc': instance.Ruc,
            'DirecionFiscal': instance.DirecionFiscal
        }