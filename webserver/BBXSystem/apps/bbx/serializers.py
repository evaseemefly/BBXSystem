from rest_framework import serializers
from .models import  BBXInfo

class BBXInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=BBXInfo
        fields=('__all__')