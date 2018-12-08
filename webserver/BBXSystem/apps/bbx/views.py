from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
import json

import datetime

# model
from .models import BBXInfo

# 序列化器
from .serializers import BBXInfoSerializer

class BBXInfoView(APIView):
    def get(self,request):
        bbxlist=BBXInfo.objects.all()
        json_data=BBXInfoSerializer(bbxlist,many=True)
        # return Response(serialize('json',bbxlist))
        return Response(json_data.data)
        # pass
