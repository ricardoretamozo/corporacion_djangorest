from rest_framework import serializers

from apps.projects.models import Projects

class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        exclude = ('modified_date','deleted_date')
    
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'created_date': instance.created_date,
            'Client_Projects': instance.Client_Projects.Persona_Nombre if instance.Client_Projects is not None else '',
            'Business_Projects': instance.Business_Projects.name if instance.Business_Projects is not None else '',
            'state': instance.state,
        }
    
    
    