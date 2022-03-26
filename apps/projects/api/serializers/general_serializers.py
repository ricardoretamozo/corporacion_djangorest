from apps.projects.models import ProjectsProduct,ProductionOrder,MaterialOrigin,MaterialsCement,MaterialsM3,MaterialsPiece,QuadrilaDay,ReinforcementSteel

from rest_framework import serializers

class ProjectsProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectsProduct
        exclude = ('state','created_date','modified_date','deleted_date')

    def to_representation(self,instance):
        
        return {
            'id': instance.id,
            'nombre': instance.Product_Projects.name if instance.Product_Projects!= '' else '' ,
            'Cantidad': instance.Cantidad,
            'empresa': instance.Project.name if instance.Project != '' else '' ,
            'plano': instance.Product_Projects.plano.url if instance.Product_Projects!= '' else '' ,
            'expediente': instance.Product_Projects.expediente_diseno.url if instance.Product_Projects!= '' else '' ,
            'molde': instance.Product_Projects.plano_molde.url if instance.Product_Projects!= '' else '' 
        }



class MaterialOriginSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialOrigin
        exclude = ('state','created_date','modified_date','deleted_date')

class MaterialsCementSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialsCement
        exclude = ('state','created_date','modified_date','deleted_date')

class MaterialsM3Serializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialsM3
        exclude = ('state','created_date','modified_date','deleted_date')

class MaterialsPieceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaterialsPiece
        exclude = ('state','created_date','modified_date','deleted_date')

class QuadrilaDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = QuadrilaDay
        exclude = ('state','created_date','modified_date','deleted_date')

class ReinforcementSteelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReinforcementSteel
        exclude = ('state','created_date','modified_date','deleted_date')

class ProductionOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductionOrder
        exclude = ('state','created_date','modified_date','deleted_date')

    def to_representation(self,instance):
        return {
            'id': instance.id,
            'usuario': instance.attendant.name if instance.attendant.name != '' else '', 
            'id_usuario': instance.attendant.id if instance.attendant.id != '' else '', 
            'date_final': instance.date_final,
            'RatioProducción': instance.RatioProducción,
            'NroMoldes': instance.NroMoldes,
            'Observacion': instance.Observacion,
        }