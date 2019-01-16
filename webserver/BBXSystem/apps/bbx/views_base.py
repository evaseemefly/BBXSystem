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
from .models import *
# 中间模型
from .middle_models import BBXDetailMidInfo,BBXStateDetailMidInfo,StateDetailMidInfo,BBXTrackMidInfo,RealtimeMidInfo
from bbxgis.models import *
from bbxgis.serializers import *

from common.DateCommon import getDataRang

# 船舶轨迹显示的最长时间（小时）
from BBXSystem.settings import BBX_TRACK_INTERVAL

# 配置文件
from BBXSystem import settings

# 序列化器
from .serializers import BBXInfoSerializer,BBXDetailInfoSerializer

# dateState_dict={
#     "normal":1.5,
#     "late":6,
#     "noarrival":24,
#     "invalid":-1
# }

dateState_dict={
    "normal":12,
    "late":18,
    "noarrival":24,
    "invalid":-1
}


class BaseView():
    '''
        通用的方法
    '''
    def getAllBBXlist(self):
        '''
            获取全部船舶的列表
        :return:
        '''
        return BBXInfo.objects.all()

    def _getStateDatetimes(self,state,nowdate):
        '''
            根据状态获取指定的起止时间
        :param state:
        :return:
        '''

        if state!='invalid':
            delayHours= dateState_dict[state]
            start,end=getDataRang(nowdate,delayHours)
        else:
            delayHours=-24
            start,end=getDataRang(nowdate,delayHours)
            end=start
        return start,end

    def _bbxTrackDatetimes(self,nowdate,interval):
        '''
            获取船舶移动轨迹的起止时间
        :param nowdate:
        :param interval:
        :return:
        '''
        return getDataRang(nowdate,interval)

class BaseTimeView():
    '''
        专门处理和船舶相关的时间的
    '''
    @property
    def nowDate(self):
        now=datetime.now()
        now=now-timedelta(hours=settings.BBX_UTC_INTERVAL)
        return now

    def utcDate(self,dt):
        '''
            获取传入时间的世界时
        :param dt:
        :return:
        '''
        dt=dt-timedelta(hours=8)
        return dt

    def localDate(self,dt):
        '''
            获取本地时间
        :param dt:
        :return:
        '''
        return dt

    # TODO 方法改为工厂方法，子类调用时，除了要传入时间以外还要穿入kind
    def getDateFactory(self,kind,dt):
        '''
            根据 local与history 获取时间
        :param kind:
        :param dt:
        :return:
        '''
        if kind=='now':
            return self.localDate(dt)
        elif kind=='history':
            return self.utcDate(dt)


    def targetDateStart(self,targetdate):
        '''
            获取指定日期的起始时间00：00
        :param targetdate:
        :return:
        '''
        # 传入的targetdate可能是一个str
        date_time = datetime.strptime(targetdate, '%Y-%m-%d')
        # 注意由于传入的targetdate是一个'yyyy-mm-dd'格式的，所以需要加入当前天的最后时刻
        date_time = date_time + timedelta(hours=00, minutes=00)
        return date_time

    def getDayLastTime(self, targetdate):
        '''
            根据传入的目标日期获取该日期的最后时刻（dt）
        :param targetdate:
        :return:
        '''
        # 传入的targetdate可能是一个str
        # 此处加入一个判断targetdate是否为dateime类型，若是str类型则转换
        if isinstance(targetdate,str):
           date_time=datetime.strptime(targetdate,'%Y-%m-%d')
        else:
            date_time=targetdate
        # 注意由于传入的targetdate是一个'yyyy-mm-dd'格式的，所以需要加入当前天的最后时刻
        date_time=date_time+timedelta(hours=23,minutes=59)
        return date_time
    @property
    def yesterDate(self):
        return self.nowDate-timedelta(hours=settings.BBX_TRACK_INTERVAL)

class BBXBaseView(BaseView):
    '''

    '''
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
        # match_date_list=[]
        for bbx_temp in bbxlist:
            stateDetailList=[]
            # 优化之前的备份
            for key in dateState_dict:
                temp_state = dateState_dict[key]
                # 获取指定状态的判断时间范围（起止时间）
                start_data, end_data = self._getStateDatetimes(key, nowdate)
                # match_date_list.push([start_data,end_data])
                # print(temp_state)
                # 先不做无效船舶的判断
                # if temp_state>0:
                # self._checkBBXMatchingLen()

                count = self._checkBBXMatchingLen(bbx_temp.bid, start_data, end_data)
                temp_detail_mid=StateDetailMidInfo(key,count)
                stateDetailList.append(temp_detail_mid)
                # else:
                #     pass
            bbx_state_detail_list.append(BBXStateDetailMidInfo(area, bbx_temp.bid,bbx_temp.code,stateDetailList))


            # index=0
            # for key in dateState_dict:
            #     index+=1
            #     temp_state = dateState_dict[key]
            #     # 获取指定状态的判断时间范围（起止时间）
            #     start_data=None
            #     end_data=None
            #     if len(match_date_list)<4:
            #         start_data, end_data = self._getStateDatetimes(key, nowdate)
            #         match_date_list.append([start_data,end_data])
            #     else:
            #         start_data=match_date_list[index-1][0]
            #         end_data = match_date_list[index - 1][0]
            #     # print(temp_state)
            #     # 先不做无效船舶的判断
            #     # if temp_state>0:
            #     # self._checkBBXMatchingLen()
            #
            #     count = self._checkBBXMatchingLen(bbx_temp.bid, start_data, end_data)
            #     temp_detail_mid=StateDetailMidInfo(key,count)
            #     stateDetailList.append(temp_detail_mid)
            #     # else:
            #     #     pass
            # bbx_state_detail_list.append(BBXStateDetailMidInfo(area, bbx_temp.bid,bbx_temp.code,stateDetailList))
        return bbx_state_detail_list

    def _checkBBXMatchingLen(self,bid,start,end):
        '''
            获取指定船舶在指定时间内的数据量
        :param bid:
        :param start:
        :param end:
        :return:
        '''

        # 根据传入的bid以及起止时间，判断bbxspacetempinfo中的记录数量
        # start<nowdate<end
        if start==end:
            list=BBXSpaceTempInfo.objects.filter(bid_id=bid,nowdate__lt=start)
        else:
            list=BBXSpaceTempInfo.objects.filter(bid_id=bid,nowdate__lte=end,nowdate__gte=start)
        count=len(list)
        return count

    def getTargetFactorList(self,bid,start,end,factor):
        '''
            获取指定船舶的指定要素观测值
        :param bid:
        :param start:
        :param end:
        :param factor:
        :return:
        '''
        # start=start-timedelta(hours=8)
        # end=end-timedelta(hours=8)

        # 对于风速与风向，要同时获取
        if factor=='ws' or factor=='wd':
            list=RealtimeData.objects.filter(bid_id=bid, timestamp__lte=end, timestamp__gte=start).values('timestamp','wd','ws')
            # list=list[:3]
            list_convert = [RealtimeMidInfo(temp['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                                {'ws':temp['ws'].__round__(2),
                                 'wd':temp['wd']})
                            for temp in list]
        else:
            list = RealtimeData.objects.filter(bid_id=bid, timestamp__lte=end, timestamp__gte=start).values('timestamp',factor)
            list_convert=[RealtimeMidInfo(temp['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),temp[factor].__round__(2)) for temp in list]
        #为了如果没得到任何结果，让屏幕显示点东西
        if len(list_convert) == 0:
            # 对于风向风速为val填充{}，其他默认填充0
            defaultAppend= lambda :{} if (factor=='wd' or factor=='ws') else 0
            dict_first = {'timestamp':start.strftime('%Y-%m-%d %H:%M:%S'),'val':defaultAppend()}
            dict_last={'timestamp':end.strftime('%Y-%m-%d %H:%M:%S'),'val':defaultAppend()}
            list_convert.append(dict_first)
            list_convert.append(dict_last)
        return list_convert
        # return RealtimeData.objects.filter(bid_id=bid,timestamp__lte=end,timestamp__gte=start).values('timestamp',factor)

    def getAllBBXlistByNow(self,targetDate):
        '''
            获取全部海区的当前24小时以内有数据的船舶列表（并去重）
        :param targetDate:
        :return:
        '''
        start,end=self._getStateDatetimes('noarrival',targetDate)
        list=BBXSpaceTempInfo.objects\
            .filter(nowdate__gte=start,nowdate__lte=end)\
            .values('bid','code')\
            .distinct()\
            .order_by('bid')

        return list


    def getAreaALLBBXBaseList(self,area):
        '''
            获取指定海区的全部志愿船集合
        :param area:
        :return:
        '''
        bbx_list=BBXInfo.objects.filter(area=area)

        return bbx_list



class BBXTrackBaseView(BaseView):
    '''
        船舶轨迹父视图
    '''
    def getAllBBXTrackList(self,targetDate):
        '''
            获取全部的船舶（有最近数据的轨迹）
        :return:
        '''
        # S1-船舶轨迹显示的最近时间长度
        BBX_TRACK_INTERVAL
        # 1-获取全部的船舶集合
        list_all_bbx=self.getAllBBXlist()
        # 2-根据全部的船舶集合获取每一条船的轨迹
        # 2-1 获取起止时间
        start,end=self._bbxTrackDatetimes(targetDate,BBX_TRACK_INTERVAL)
        list_bbxtrack=[]
        for temp in list_all_bbx:
            latlngs=[]
            list_track=BBXSpaceTempInfo.objects.filter(nowdate__lte=end,nowdate__gte=start,bid_id=temp.bid)
            # 提取该track的经纬度到一个集合中
            # 注意此处存在一个bug，若列表推导，使用{temp_track.lat,temp_track.lon}
            # 顺序有时会出现颠倒的状况
            # 字典为无序集合，使用数组解决问题
            # latlngs=[
            #     [temp_track.lat,temp_track.lon]
            # for temp_track in list_track]

            # latlngs = [
            #     ([temp_track.lat, temp_track.lon] if (temp_track.lat==9999 or temp_track.lon==9999) else [])
            #     for temp_track in list_track]

            # 注意此处不能向前台传递[]空的部分，使用最后的方式
            # latlngs=[
            #     [] if (temp_track.lat==9999 or temp_track.lon==9999) else [temp_track.lat,temp_track.lon]
            # for temp_track in list_track]

            latlngs = [
                [temp_track.lat, temp_track.lon]
                for temp_track in list_track
                if temp_track.lat!=9999 and temp_track.lon!=9999]


            # for temp_track in list_track:
            #     if temp_track.lat==9999 or temp_track.lng==9999:
            #         []
            list_bbxtrack.append(BBXTrackMidInfo(temp.code,temp.bid,latlngs))
        return list_bbxtrack

