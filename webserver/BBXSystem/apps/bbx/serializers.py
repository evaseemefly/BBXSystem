from rest_framework import serializers
from .models import  BBXInfo

class BBXInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=BBXInfo
        fields=('__all__')

class BBXDetailInfoSerializer(serializers.Serializer):
    '''
        海区及船舶集合
    '''
    area=serializers.CharField()
    bbxlist=BBXInfoSerializer(many=True)