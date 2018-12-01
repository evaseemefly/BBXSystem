from django.db import models

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