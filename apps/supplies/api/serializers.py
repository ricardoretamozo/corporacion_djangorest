from rest_framework import serializers

from apps.supplies.models import Supplies

class SuppliesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplies
        exclude = ('state','created_date','modified_date','deleted_date')