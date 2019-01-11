from django.http import HttpRequest,HttpResponse,JsonResponse,Http404
from datetime import datetime,timedelta
from functools import wraps
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
# 为视图使用的自定义装饰器

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
            targetdate = targetdate if targetdate is not None else datetime.now().strftime('%Y-%m-%d')
            isNow=request.GET.get('isNow',True)
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



def history_requeired(func):
    '''
        实时历史数据装饰器
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
#
# def date_required(view):
#
#     def decorator(request,*args,**kwargs):
#         targetdate = request.GET.get('targetdate',None)
#         targetdate = targetdate if targetdate is not None else datetime.now().strftime('%Y-%m-%d')