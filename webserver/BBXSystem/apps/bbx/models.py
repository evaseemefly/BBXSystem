from django.db import models
import datetime
from datetime import datetime
# Create your models here.


class BBXInfo(models.Model):
    '''
        船舶基础信息
    '''
    CHOICE_AREA=(
        ('n','北海'),
        ('e','东海'),
        ('s','南海')
    )
    CHOICE_SHOPTYPE=(
        ('s','小型'),
        ('m','中型'),
        ('l','大型')
    )
    bid=models.AutoField(primary_key=True)

    code=models.CharField(max_length=10,default='')
    area=models.CharField(choices=CHOICE_AREA,verbose_name="所属海区",max_length=2)
    desc=models.CharField(max_length=200,verbose_name="描述信息")
    shipton=models.FloatField(default=100,verbose_name="吨位-单位百万",max_length=4)
    shiptype=models.CharField(choices=CHOICE_SHOPTYPE,verbose_name="船型",max_length=2)
    sort=models.IntegerField(default=99,verbose_name="排序")
    class Meta:
        verbose_name=u"船舶基础信息"
        verbose_name_plural=verbose_name

class BBXSpaceInfo(models.Model):
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

class BBXSpaceTempInfo(models.Model):
    '''
        船舶基础数据（临时表）
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
        verbose_name=u"船舶基础数据（临时表）"
        verbose_name_plural=verbose_name

class RealtimeData(models.Model):
    '''
        志愿船的水文气象要素（临时表）
    '''
    rdid=models.AutoField(primary_key=True)
    bid = models.ForeignKey(BBXInfo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, verbose_name="时间戳")
    rain = models.FloatField(max_length=10, null=True, verbose_name="降水")
    vis = models.FloatField(max_length=10, null=True, verbose_name="能见度")
    cloudc = models.FloatField(max_length=10, null=True, verbose_name="云量")
    wd = models.FloatField(max_length=10, null=True, verbose_name="风向")
    ws = models.FloatField(max_length=10, null=True, verbose_name="风速")
    cwd = models.FloatField(max_length=10, null=True, verbose_name="最大风向")
    cws = models.FloatField(max_length=10, null=True, verbose_name="最大风速")
    at = models.FloatField(max_length=4, null=True, verbose_name="气温")
    dpt = models.FloatField(max_length=10, null=True, verbose_name="露点温度")
    bp = models.FloatField(max_length=10, null=True, verbose_name="气压")
    wetnow = models.FloatField(max_length=10, null=True, verbose_name="当前湿度")
    wet1 = models.FloatField(max_length=10, null=True, verbose_name="湿度1")
    wet2 = models.FloatField(max_length=10, null=True, verbose_name="湿度2")
    cloudlc = models.FloatField(max_length=10, null=True, verbose_name="云总量")
    clouds = models.FloatField(max_length=10, null=True, verbose_name="云状")
    cloudms = models.FloatField(max_length=10, null=True, verbose_name="")
    cloudhs = models.FloatField(max_length=10, null=True, verbose_name="云高")
    wt = models.FloatField(max_length=4, null=True, verbose_name="水温")
    wvs = models.FloatField(max_length=4, null=True, verbose_name="浪向")
    wv = models.FloatField(max_length=4, null=True, verbose_name="浪高")
    surge1d = models.FloatField(max_length=4, null=True, verbose_name="第一组涌向")
    surge1c = models.FloatField(max_length=4, null=True, verbose_name="第一组涌周期")
    surge1h = models.FloatField(max_length=4, null=True, verbose_name="第一组涌高")
    surge2d = models.FloatField(max_length=4, null=True, verbose_name="第二组涌向")
    surge2c = models.FloatField(max_length=4, null=True, verbose_name="第二组涌周期")
    surge2h = models.FloatField(max_length=4, null=True, verbose_name="第二组涌向")

    class Meta:
        verbose_name = u"志愿船的水文气象要素（临时表）"
        verbose_name_plural = verbose_name

class MeteorologicalData(models.Model):
    '''
        气象要素历史表
    '''
    mid=models.AutoField(primary_key=True)
    bid = models.ForeignKey(BBXInfo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, verbose_name="时间戳")
    rain=models.FloatField(max_length=10,null=True,verbose_name="降水")
    vis=models.FloatField(max_length=10,null=True,verbose_name="能见度")
    cloudc=models.FloatField(max_length=10,null=True,verbose_name="云量")
    wd=models.FloatField(max_length=10,null=True,verbose_name="风向")
    ws=models.FloatField(max_length=10,null=True,verbose_name="风速")
    cwd=models.FloatField(max_length=10,null=True,verbose_name="最大风向")
    cws=models.FloatField(max_length=10,null=True,verbose_name="最大风速")
    at=models.FloatField(max_length=4,null=True,verbose_name="气温")
    dpt=models.FloatField(max_length=10,null=True,verbose_name="露点温度")
    bp=models.FloatField(max_length=10,null=True,verbose_name="气压")
    wetnow=models.FloatField(max_length=10,null=True,verbose_name="当前湿度")
    wet1=models.FloatField(max_length=10,null=True,verbose_name="湿度1")
    wet2=models.FloatField(max_length=10,null=True,verbose_name="湿度2")
    cloudlc=models.FloatField(max_length=10,null=True,verbose_name="云总量")
    clouds=models.FloatField(max_length=10,null=True,verbose_name="云状")
    cloudms=models.FloatField(max_length=10,null=True,verbose_name="")
    cloudhs=models.FloatField(max_length=10,null=True,verbose_name="云高")
    class Meta:
        verbose_name=u"气象要素"
        verbose_name_plural=verbose_name

class HydrologyData(models.Model):
    '''
        水文要素历史表
    '''
    hid=models.AutoField(primary_key=True)
    bid = models.ForeignKey(BBXInfo, on_delete=models.CASCADE)
    wt=models.FloatField(max_length=4,null=True,verbose_name="水温")
    wvs=models.FloatField(max_length=4,null=True,verbose_name="浪向")
    wv=models.FloatField(max_length=4,null=True,verbose_name="浪高")
    surge1d=models.FloatField(max_length=4,null=True,verbose_name="第一组涌向")
    surge1c=models.FloatField(max_length=4,null=True,verbose_name="第一组涌周期")
    surge1h=models.FloatField(max_length=4,null=True,verbose_name="第一组涌高")
    surge2d=models.FloatField(max_length=4,null=True,verbose_name="第二组涌向")
    surge2c=models.FloatField(max_length=4,null=True,verbose_name="第二组涌周期")
    surge2h=models.FloatField(max_length=4,null=True,verbose_name="第二组涌向")
    class Meta:
        verbose_name=u"水文要素历史表"
        verbose_name_plural=verbose_name