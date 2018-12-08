from rest_framework import serializers
from .models import  BBXGeoInfo

class BBXGeoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=BBXGeoInfo
        fields=('__all__')