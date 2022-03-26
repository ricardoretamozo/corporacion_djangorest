from rest_framework import serializers

from apps.products.models import Products
from django.conf.urls.static import static
from django.conf import settings

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        exclude = ('state','created_date','modified_date','deleted_date')
    
    """
    def to_representation(self,instance):
        print(instance)
        print(settings.MEDIA_URL)
        print(settings.MEDIA_ROOT)
        print(static)
        return {
            'id': instance.id,
            'name': instance.name,
            'plano': instance.plano.name if instance.plano.name != '' else '',
            'expediente_diseno': instance.expediente_diseno.name if instance.expediente_diseno.name != '' else '',
            'plano_molde': instance.plano_molde.name if instance.plano_molde.name != '' else '',
            'Costo_Produccion': instance.Costo_Produccion,
            'Business_Products': instance.Business_Products.name if instance.Business_Products is not None else ''
        }
    """

    