from django.conf.urls import url, include
from .views import BBXInfoView

app_name='[gis]'
urlpatterns = [
    #获取指定日期的预报数据
    url(r'^bbxlist/$', BBXInfoView.as_view(), name="gis-get-bbxlist")
]