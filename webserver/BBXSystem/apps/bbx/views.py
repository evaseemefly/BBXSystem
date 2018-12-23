from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.core import serializers
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.db.models import Q
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.db.models import Max
from rest_framework import status
import json

from datetime import datetime,timedelta
import time
import pytz

# model
from .models import BBXInfo,BBXSpaceTempInfo
# 中间模型
from .middle_models import BBXDetailMidInfo
from bbxgis.models import *
from bbxgis.serializers import *

# 序列化器
from .serializers import BBXInfoSerializer,BBXDetailInfoSerializer

# 父类视图层
from .views_base import BBXBaseView

# 海区元祖
area_tup=(
    'n',
    'e',
    's'
)

class BBXInfoView(APIView):
    '''

    '''
    def get(self,request):
        bbxlist=BBXInfo.objects.all()
        json_data=BBXInfoSerializer(bbxlist,many=True)
        # return Response(serialize('json',bbxlist))
        return Response(json_data.data)
        # pass

class BBXAllListView(APIView):
    '''
        获取三个海区的船舶列表
    '''
    def get(self,request):
        bbxAllList=[]
        # 分别根据三海区循环获取对应的船舶
        for i in range(len(area_tup)):
            print(area_tup[i])

            bbxAllList.append(BBXDetailMidInfo(area_tup[i],self.getAreaAllBBXList(area_tup[i])))

        json_data=BBXDetailInfoSerializer(bbxAllList,many=True).data
        return Response(json_data)
        pass

    def getAreaAllBBXList(self,area):
        '''
            获取指定海区的全部船舶列表
        :param area:
        :return:
        '''
        bbx_list=BBXInfo.objects.filter(area=area)
        return bbx_list


class BBXStateListView(APIView,BBXBaseView):
    def get(self,request):
        test_date = '2018-09-20'
        test_date = datetime.strptime(test_date, '%Y-%m-%d')
        list= self.getBBXStateListbyArea('n',test_date)
        pass


class BBXAllStateListView(APIView):
    '''
        获取三个海区的船舶最新状态的列表
    '''
    def get(self,request):
        pass





def getBaseState(request,area=None,nowDate=''):
    if area is None and nowDate is None:
        return HttpRequest('parameters is not enough')
    try:
        d = datetime.strptime(nowDate,'%Y-%m-%d %H:%M')
    except Exception as err:
        d = datetime.now()
    # 好像是时区问题所以必须加8小时才行
    d = d.astimezone(pytz.UTC)+timedelta(hours=8)
    bbxinfolist = BBXInfo.objects.all()
    timelimit =d.__str__()
    lst =[]
    print(timelimit.__str__(),nowDate)
    for x in bbxinfolist:
        dic = dict()
        dic['code']=x.code
        dic['name']=x.code
        dt=x.bbxspacetempinfo_set.filter(nowdate__lte=timelimit).aggregate(Max('nowdate'))
        if dt['nowdate__max'] is not None:
            dic['state'] = dt['nowdate__max']
        else:
            dic['state']='invalid'
        lst.append(dic)

    ok_seconds = 1.5*60*60
    late_seconds=6*60*60


    #根据日期判断状态
    for x in lst:
        state = x['state']
        if state != 'invalid':
            nowdateDelta = d-state
            if nowdateDelta.seconds>ok_seconds:
                if nowdateDelta.seconds>late_seconds:
                    state='noarrival'
                else:
                    state='late'
            else:
                state='ok'
        x['state']=state
    return HttpResponse(json.dumps(lst),content_type="application/json")


def getShipListBySeaArea(request,seaAreas=''):
    seaAreas=seaAreas.split(',')
    bbxlist = BBXInfo.objects.filter(area__in=seaAreas).all()
    jsonData = BBXInfoSerializer(bbxlist,many=True)
    return HttpResponse(jsonData.data,content_type="application/json")

#测试的时候先都用entity回头再写middle
#暂时有问题
def getShipStateByShips(request,ships=''):
    ships=ships.split(',')
    shipinfoes = BBXSpaceTempInfo.objects.filter(bid__code__in=ships)
    jsonData = BBXSpaceTempInfoSerializer(shipinfoes,many=True)
    return HttpResponse(jsonData.data,content_type="application/json")
