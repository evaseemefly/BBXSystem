from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.db.models import Q
# from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
import json

import datetime

# 引入models
from .models import BBXGeoInfo

# 序列化器
from .serializers import BBXGeoInfoSerializer
# Create your views here.

class BBXSpaceInfoView(APIView):
    def get(self,request):
        bbxlist=BBXGeoInfo.objects.all()
        json_geo= serialize('geojson',bbxlist)
        # 需要手动去掉/
        # new_json_geo=str.replace(json_geo,'\\','')
        # json_geo = BBXGeoInfoSerializer(bbxlist,many=True)
        # return JsonResponse(new_json_geo)
        return HttpResponse(json_geo)
