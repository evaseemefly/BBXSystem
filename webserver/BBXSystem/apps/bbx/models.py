from django.db import models
import datetime
# Create your models here.
class BBXInfo(models.Model):
    '''
        海洋站详情
    '''
    id=models.AutoField(primary_key=True)
    # 父级节点
    pid=models.IntegerField(default=0)
    name=models.CharField(max_length=50,verbose_name=u"海洋站名称")
    code=models.CharField(max_length=6,verbose_name=u"海洋站站代码")
    area=models.CharField(max_length=2,choices=(("n","北海"),("e","东海"),("s","南海")),verbose_name="所属区域")
    Lon=models.FloatField(max_length=6,verbose_name="经度")
    Lat=models.FloatField(max_length=6,verbose_name="维度")
    remark = models.CharField(max_length=200, verbose_name=u"备注", null=True)
    class Meta:
        verbose_name=u"海洋站信息"
        verbose_name_plural=verbose_name

class BBXSpaceInfo(models.Model):
    '''
        船舶基础数据（空间信息）
    '''
    bsid=models.AutoField(primary_key=True)
    biid=models.ForeignKey('')
    code=models.CharField(max_length=10,default='')
    nowdate=models.DateTimeField(default=datetime.now)
    lat=models.FloatField(max_length=6,verbose_name="经度")
    lon=models.FloatField(max_length=6,verbose_name="维度")
    heading=models.FloatField(null=True,verbose_name="船首向")
    speed=models.FloatField(null=True,verbose_name="速度")

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
        ('m'.'中型'),
        ('l','大型')
    )
    biid=models.AutoField(primary_key=True)
    code=models.CharField(max_length=10,default='')
    area=models.CharField(choices=CHOICE_AREA)
    desc=models.CharField(max_length=200)
    shipton=models.FloatField(default=100)
    shiptype=models.CharField(choices=CHOICE_SHOPTYPE)
    sort=models.IntegerField(default=99)

class MeteorologicalData(models.Model):
    '''
        气象要素
    '''
    mid=models.AutoField(primary_key=True)
    rain=models.FloatField(max_length=10,null=True)
    vis=models.FloatField(max_length=10,null=True)
    cloudc=models.FloatField(max_length=10,null=True)
    wd=models.FloatField(max_length=10,null=True)
    ws=models.FloatField(max_length=10,null=True)
    cwd=models.FloatField(max_length=10,null=True)
    cws=models.FloatField(max_length=10,null=True)
    at=models.FloatField(max_length=4,null=True)
    dpt=models.FloatField(max_length=10,null=True)
    bp=models.FloatField(max_length=10,null=True)
    wetnow=models.FloatField(max_length=10,null=True)
    wet1=models.FloatField(max_length=10,null=True)
    wet2=models.FloatField(max_length=10,null=True)
    cloudc=models.IntegerField(max_length=10,null=True)
    clouds=models.FloatField(max_length=10,null=True)
    cloudms=models.FloatField(max_length=10,null=True)
    cloudhs=models.FloatField(max_length=10,null=True)

class HydrologyData(models.Model):
    '''
        水文要素
    '''
    hid=models.AutoField(primary_key=True)
    wt=models.FloatField(max_length=4,null=True)
    wvs=models.FloatField(max_length=4,null=True)
    wv=models.FloatField(max_length=4,null=True)
    surge1d=models.FloatField(max_length=4,null=True)
    surge1c=models.FloatField(max_length=4,null=True)
    surge1h=models.FloatField(max_length=4,null=True)
    surge2d=models.FloatField(max_length=4,null=True)
    surge2c=models.FloatField(max_length=4,null=True)
    surge2h=models.FloatField(max_length=4,null=True)