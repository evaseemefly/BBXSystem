from rest_framework import serializers
from .models import  BBXInfo,RealtimeData

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

class BBXSimpInfoSerializer(serializers.Serializer):
    '''
        精简版的船舶
        只包含code bid
    '''
    bid=serializers.IntegerField()
    code=serializers.CharField()

class BBXSimpDetailInfoSerializer(serializers.Serializer):
    '''
        海区及船舶集合
    '''
    area=serializers.CharField()
    bbxlist=BBXSimpInfoSerializer(many=True)

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

class RealtimeSimpSerializer(serializers.Serializer):
    timestamp=serializers.DateTimeField()
    val=serializers.FloatField()
    # val = serializers.DictField()

class RealtimeWdWsSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    # val=serializers.FloatField()
    val = serializers.DictField()
    # class Meta:
    #     model=RealtimeData
    #     fields=('__all__')
