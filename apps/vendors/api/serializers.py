from rest_framework import serializers

from apps.vendors.models import Vendors

class VendorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendors
        exclude = ('state','created_date','modified_date','deleted_date')