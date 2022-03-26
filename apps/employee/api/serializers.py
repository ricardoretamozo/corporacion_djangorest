from rest_framework import serializers
from apps.business.api.serializers.business_serializers import BusinessSerializer
from apps.employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        exclude = ('state','created_date','modified_date','deleted_date')

    def to_representation(self,instance):
        return {
            'id': instance.id,
            'DNI': instance.DNI,
            'name': instance.name,
            'last_name':instance.last_name,
            'Rol': instance.Rol,
            'Business_Employee': instance.Business_Employee.name if instance.Business_Employee is not None else ''
        }