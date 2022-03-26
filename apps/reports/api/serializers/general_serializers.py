from rest_framework import serializers

from apps.reports.models import Materials,Tareo,Endurancetest,AirForce,ServiceRequirement,ProductService

class MaterialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materials
        exclude = ('state','created_date','modified_date','deleted_date')

class TareoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tareo
        exclude = ('state','created_date','modified_date','deleted_date')

class EndurancetestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endurancetest
        exclude = ('state','created_date','modified_date','deleted_date')

class AirForceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirForce
        exclude = ('state','created_date','modified_date','deleted_date')

class ServiceRequirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceRequirement
        exclude = ('state','created_date','modified_date','deleted_date')

class ProductServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductService
        exclude = ('state','created_date','modified_date','deleted_date')
