from rest_framework import serializers

from apps.reports.models import Reports

class ReportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reports
        exclude = ('state','created_date','modified_date','deleted_date')