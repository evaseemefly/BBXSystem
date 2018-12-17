from django.conf.urls import url, include
from .views import BBXSpaceInfoView,GPSDataView,BBXTrackView

app_name='[gis]'
urlpatterns = [
    #获取指定日期的预报数据
    url(r'^bbxspace/$', BBXSpaceInfoView.as_view(), name="gis-get-bbxspace"),
    url(r'^gps/$', GPSDataView.as_view(), name="gis-get-gps"),
    url(r'^track/$',BBXTrackView.as_view(),name="gis-get-track")
]