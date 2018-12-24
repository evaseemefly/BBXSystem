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

class StateDetailMidSerializer(serializers.Serializer):
    state=serializers.CharField()
    count=serializers.IntegerField()

class BBXStateDetailMidSerializer(serializers.Serializer):
    bid=serializers.IntegerField()
    code=serializers.CharField()
    area=serializers.CharField()
    stateDetailList=StateDetailMidSerializer(many=True)

class AreaStatisticMidInfoSerializer(serializers.Serializer):
    state=serializers.CharField()
    count=serializers.IntegerField()
    list=serializers.ListField()

class StatisticMidInfoSerializer(serializers.Serializer):
    area=serializers.CharField()
    static=AreaStatisticMidInfoSerializer(many=True)

class BBXTrackMidInfoSerializer(serializers.Serializer):
    code=serializers.CharField()
    bid=serializers.IntegerField()
    latlngs=serializers.ListField()

