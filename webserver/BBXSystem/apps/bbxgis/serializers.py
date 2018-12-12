from rest_framework import serializers
from .models import  BBXGeoInfo

class BBXGeoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=BBXGeoInfo
        fields=('__all__')


class GeometrySerializer(serializers.Serializer):
    type=serializers.CharField()
    coordinates=serializers.ListField()

class PropertySerializer(serializers.Serializer):
    time=serializers.ListField()

class GPSDataSerializer(serializers.Serializer):
    type=serializers.CharField()
    geometry=GeometrySerializer()
    properties=PropertySerializer()
    bbox=serializers.ListField()

class BBXTrackSerializer(serializers.Serializer):
    '''
        船舶轨迹
    '''
    bsid=serializers.IntegerField()
    code=serializers.CharField()
    starttime=serializers.DateTimeField()
    endtime=serializers.DateTimeField()
    latlngs=serializers.ListField()
    speeds=serializers.ListField()
