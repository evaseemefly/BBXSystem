from django.db import models
from datetime import datetime
from django.contrib.gis.db import models
from bbx.models import BBXInfo
# Create your models here.

# class BBXGeoInfo(models.Model):
#     point=models.PointField(null=True,blank=True)

class BBXGeoInfo(models.Model):
    '''
        船舶基础数据（空间信息）
    '''
    bsid=models.AutoField(primary_key=True)
    bid=models.ForeignKey(BBXInfo,on_delete=models.CASCADE)
    code=models.CharField(max_length=10,default='')
    nowdate=models.DateTimeField(default=datetime.now)
    lat=models.FloatField(max_length=6,verbose_name="经度")
    lon=models.FloatField(max_length=6,verbose_name="维度")
    heading=models.FloatField(null=True,verbose_name="船首向")
    speed=models.FloatField(null=True,verbose_name="速度")
    class Meta:
        verbose_name=u"船舶基础数据（空间信息）"
        verbose_name_plural=verbose_name