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
import pytz

# model
from .models import BBXInfo,BBXSpaceTempInfo
# 中间模型
from .middle_models import BBXDetailMidInfo,BBXStateDetailMidInfo,StateDetailMidInfo
from bbxgis.models import *
from bbxgis.serializers import *

from common.DateCommon import getDataRang


# 序列化器
from .serializers import BBXInfoSerializer,BBXDetailInfoSerializer

dateState_dict={
    "normal":1.5,
    "late":6,
    "noarrival":24,
    "invalid":-1
}

class BBXBaseView():
    def getBBXStateListbyArea(self,area,nowdate):
        '''
            根据海区查询该海区所有船舶的传输状态
        :param area:
        :return:
        '''

        # 1-获取时间范围
        start_data=nowdate
        end_data=nowdate
        bbx_state_detail_list=[]
        # for key in dateState_dict:
        #     tempState=dateState_dict[key]
        #     print(tempState)
        #     if tempState>0:
        #         pass
        #         start_data,end_data=self.getStateDatetimes(key,nowdate)
        #         # 2- 根据起止时间进行筛选
        #         # 2-1 获取该海区的所有bbx基础列表
        #         bbxlist= self.getAreaALLBBXBaseList(area)
        #         # 2-2 对所有的船舶进行判断
        #         for bbxtemp in bbxlist:
        #             count= self.checkBBXMatchingLen(bbxtemp.bid,start_data,end_data)
        #             bbx_state_detail_list.append(BBXStateDetailMidInfo(area,bbxtemp.bid,key,count))
        #     else:
        #         pass

        # 2- 根据起止时间进行筛选
        # 2-1 获取该海区的所有bbx基础列表
        bbxlist = self.getAreaALLBBXBaseList(area)
        for bbx_temp in bbxlist:
            stateDetailList=[]
            for key in dateState_dict:
                temp_state = dateState_dict[key]
                start_data, end_data = self.getStateDatetimes(key, nowdate)
                # print(temp_state)
                if temp_state>0:
                    count = self.checkBBXMatchingLen(bbx_temp.bid, start_data, end_data)
                    temp_detail_mid=StateDetailMidInfo(key,count)
                    stateDetailList.append(temp_detail_mid)
            bbx_state_detail_list.append(BBXStateDetailMidInfo(area, bbx_temp.bid,bbx_temp.code,stateDetailList))
        return bbx_state_detail_list

    def checkBBXMatchingLen(self,bid,start,end):
        '''
            获取指定船舶在指定时间内的数据量
        :param bid:
        :param start:
        :param end:
        :return:
        '''

        # 根据传入的bid以及起止时间，判断bbxspacetempinfo中的记录数量
        # start<nowdate<end
        list=BBXSpaceTempInfo.objects.filter(bid_id=bid,nowdate__lte=end,nowdate__gte=start)
        count=len(list)
        return count


    def getAreaALLBBXBaseList(self,area):
        '''
            获取指定海区的全部志愿船集合
        :param area:
        :return:
        '''
        bbx_list=BBXInfo.objects.filter(area=area)

        return bbx_list

    def getStateDatetimes(self,state,nowdate):
        '''
            根据状态获取指定的起止时间
        :param state:
        :return:
        '''
        delayHours= dateState_dict[state]

        return getDataRang(nowdate,delayHours)