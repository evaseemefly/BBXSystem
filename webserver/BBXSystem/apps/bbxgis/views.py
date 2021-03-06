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

# 引入models
from .models import BBXGeoInfo

from .middle_models import Geometry,GPSData,Property,BBXTrack

# 序列化器
from .serializers import BBXGeoInfoSerializer,GPSDataSerializer,BBXTrackSerializer
# Create your views here.

class BBXSpaceInfoView(APIView):
    def get(self,request):
        bbxlist=BBXGeoInfo.objects.all()
        # json_geo= serialize('json',bbxlist)
        # 需要手动去掉/
        #  new_json_geo=str.replace(json_geo,'\\','')
        json_geo = BBXGeoInfoSerializer(bbxlist,many=True)
        # data=json.loads
        # return JsonResponse(json_geo)
        return Response(json_geo.data)

class BBXTrackView(APIView):
    '''
        船舶轨迹视图
        fun：
            1-根据传入的时间，获取当前时间的基准时间，并获取起止时间（72h前，now）
            2-
    '''
    # 舍弃以下测试数据
    # def get(self,request):
    #     # 创建一组测试数据
    #     latlngs=[[44.63, -123.47], [46.63, -123.47], [46.63, -119.47]]
    #     latlngs_2=[[45.63, -122.47], [43.63, -121.47], [44.63, -119.27]]
    #     latlngs_3 = [[43.63, -121.47], [43.93, -122.17], [44.43, -119.27]]
    #     speeds=[5.2,5.2,5.2,5.2]
    #     speeds_1 = [5.2, 5.2, 5.2, 5.2]
    #     speeds_3 = [5.2, 5.2, 5.2, 5.2]
    #     bbx_track= BBXTrack(123,'BBXA','2018-12-11 10:00','2018-12-11 10:00',latlngs,speeds)
    #     bbx_track_2 = BBXTrack(123, 'BBXB', '2018-12-11 10:00', '2018-12-11 10:00', latlngs_2, speeds_1)
    #     bbx_track_3 = BBXTrack(123, 'BBXC', '2018-12-11 10:00', '2018-12-11 10:00', latlngs_3, speeds_3)
    #     json_data=BBXTrackSerializer([bbx_track,bbx_track_2,bbx_track_3],many=True).data
    #     # json_data = BBXTrackSerializer([bbx_track], many=True).data
    #     return Response(json_data)
    def get(self,request):

        # 创建一组测试数据
        latlngs=[[44.63, -123.47], [46.63, -123.47], [46.63, -119.47]]
        latlngs_2=[[45.63, -122.47], [43.63, -121.47], [44.63, -119.27]]
        latlngs_3 = [[43.63, -121.47], [43.93, -122.17], [44.43, -119.27]]
        speeds=[5.2,5.2,5.2,5.2]
        speeds_1 = [5.2, 5.2, 5.2, 5.2]
        speeds_3 = [5.2, 5.2, 5.2, 5.2]
        bbx_track= BBXTrack(123,'BBXA','2018-12-11 10:00','2018-12-11 10:00',latlngs,speeds)
        bbx_track_2 = BBXTrack(123, 'BBXB', '2018-12-11 10:00', '2018-12-11 10:00', latlngs_2, speeds_1)
        bbx_track_3 = BBXTrack(123, 'BBXC', '2018-12-11 10:00', '2018-12-11 10:00', latlngs_3, speeds_3)
        json_data=BBXTrackSerializer([bbx_track,bbx_track_2,bbx_track_3],many=True).data
        # json_data = BBXTrackSerializer([bbx_track], many=True).data
        return Response(json_data)

class GPSDataView(APIView):
    '''
        暂时不使用了
    '''
    def get(self,request):
        geo_temp=Geometry([[-123.4726739,44.61131534],[-123.47325805,44.61110968]])
        pro_temp=Property([1369786338000,1369786340000])
        bbox_temp=[[-123.55229844, 44.53998806],[-123.55229844, 44.61162111]]
        gps_temp=GPSData(geo_temp,pro_temp,bbox_temp)

        json_data=GPSDataSerializer(gps_temp)
        print(json_data.data)
        return Response(json_data.data)
        pass


