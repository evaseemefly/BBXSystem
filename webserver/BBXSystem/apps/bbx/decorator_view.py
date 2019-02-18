from django.http import HttpRequest,HttpResponse,JsonResponse,Http404
from datetime import datetime,timedelta
from functools import wraps
from django.core.exceptions import ObjectDoesNotExist
from pytz import timezone
from django.utils import timezone
from django.utils.timezone import utc
from django.http import HttpResponseRedirect
# 为视图使用的自定义装饰器
import pytz
# 自己的一些组件
from common import DateCommon

sct_tz=pytz.timezone('Asia/Shanghai')

def date_required(func):
    '''
        目标时间装饰器，若request中未含targetdate，则将当前日期付给requset
    :param func:
    :return:
    '''
    @wraps(func)
    def returned_wrapper(request, *args, **kwargs):
        try:
            targetdate = request.GET.get('targetdate', None)
            kind= request.GET.get('kind','now')
            utcnow=datetime.utcnow().replace(tzinfo=utc)
            # targetdate = targetdate if kind=='history' else datetime.now()
            targetdate = targetdate if kind == 'history' else utcnow
            if kind=='now':
                # now str转成 yyyy-mm-dd HH:mm
                # targetdate.strftime('%Y-%m-%d %H:%M')
                pass
            elif kind=='history':
                # history str时转成 yyyy-mm-dd
                # TODO 此处若为history时，例如将 '2019-01-03' 转换为utc时间时，时间并未减8
                targetdate=datetime.strptime(targetdate,'%Y-%m-%d').replace(tzinfo=utc)
                targetdate=targetdate+timedelta(hours=-8)
                tzname = timezone.get_current_timezone_name()
                # targetdate=pytz.timezone(tzname).localize(targetdate)

            # 转换为世界时
            # targetdate=DateCommon.local2Utc(targetdate)
            # isNow=request.GET.get('isNow',True)
            request.GET=request.GET.copy()
            request.GET['targetdate']=targetdate
            return func(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise Http404()
            # if redirect:
            #     return HttpResponseRedirect(redirect)
            # else:
            #     raise Http404()

    return returned_wrapper
    # def decorator(func):
    #     @wraps(func)
    #     def returned_wrapper(request, *args, **kwargs):
    #         try:
    #             targetdate = request.GET.get('targetdate', None)
    #             targetdate = targetdate if targetdate is not None else datetime.now().strftime('%Y-%m-%d')
    #             return func(request, *args, **kwargs)
    #         except ObjectDoesNotExist:
    #             if redirect:
    #                 return HttpResponseRedirect(redirect)
    #             else:
    #                 raise Http404()
    #     return returned_wrapper
    # return decorator

def data_loaclUtc(func):
    '''
        将本地时间转换为世界时
    :param func:
    :return:
    '''
    @wraps(func)
    def returned_wrapper(request, *args, **kwargs):
        try:
            targetdate = request.GET.get('targetdate', None)
            # 转为世界时
            utcDate=DateCommon.local2Utc(targetdate)
            request.GET = request.GET.copy()
            request.GET['targetdate'] = utcDate
            return func(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise Http404()
            # if redirect:
            #     return HttpResponseRedirect(redirect)
            # else:
            #     raise Http404()

    return returned_wrapper

def history_requeired(func):
    '''
        实时历史数据装饰器
        请求中若未包含kind，则默认赋值给now（获取当前）
    :param func:
    :return:
    '''
    @wraps(func)
    def returned_wrapper(request, *args, **kwargs):
        try:
            kind=request.GET.get('kind','now')
            request.GET=request.GET.copy()
            request.GET['kind']=kind
            return func(request, *args, **kwargs)
        except ObjectDoesNotExist:
            raise Http404()
            # if redirect:
            #     return HttpResponseRedirect(redirect)
            # else:
            #     raise Http404()

    return returned_wrapper