from django.conf.urls import url, include
from django.urls import path
from .views import BBXInfoView,BBXAllListView,BBXStateListView,AreaStatisticView,BBXGPSTrackView,RealtimeListView
from . import views

app_name='[gis]'
urlpatterns = [
    #获取指定日期的预报数据
    url(r'^bbxlist/$', BBXInfoView.as_view(), name="gis-get-bbxlist"),
    # 获取所有海区的志愿船列表
    url(r'^areaalllist/$',BBXAllListView.as_view()),
    url(r'^bbxstatelist/$',BBXStateListView.as_view()),
    url(r'^areastatelist/$',AreaStatisticView.as_view()),
    url(r'^track/$',BBXGPSTrackView.as_view()),
    url(r'^facotrlist/$',RealtimeListView.as_view()),
    path('GetBaseState/<str:area>/<str:nowDate>',views.getBaseState),
    path('GetBaseState/<str:area>/',views.getBaseState)
]
