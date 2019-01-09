from django.http import HttpRequest,HttpResponse,JsonResponse,Http404
from datetime import datetime,timedelta
from functools import wraps
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
# 为视图使用的自定义装饰器

def date_required(func):
    @wraps(func)
    def returned_wrapper(request, *args, **kwargs):
        try:
            targetdate = request.GET.get('targetdate', None)
            targetdate = targetdate if targetdate is not None else datetime.now().strftime('%Y-%m-%d')
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

#
# def date_required(view):
#
#     def decorator(request,*args,**kwargs):
#         targetdate = request.GET.get('targetdate',None)
#         targetdate = targetdate if targetdate is not None else datetime.now().strftime('%Y-%m-%d')