from apps.business.models import Campus
from apps.business.api.serializers.business_serializers import BusinessSerializer
from rest_framework import serializers

class CampusSerializer(serializers.ModelSerializer):
    Business_Campus = BusinessSerializer()
    #Business_Campus = serializers.StringRelatedField()
    class Meta:
        model = Campus
        exclude = ('state','created_date','modified_date','deleted_date')