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

