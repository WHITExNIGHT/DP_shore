from django.db import models
from tinymce.models import HTMLField
import django.utils.timezone as timezone


class TypeInfo(models.Model):
    ttitle = models.CharField('标题', max_length=20)
    isDelete = models.BooleanField('删除', default=False)

    def __str__(self):
        return self.ttitle

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = '类型'


class ImgInfo(models.Model):
    ititle = models.CharField('标题', max_length=20)
    iimg = models.ImageField('图片', upload_to='dp_imgs')
    isDelete = models.BooleanField('删除', default=False)
    iclick = models.IntegerField('点击量', default=0)
    icontent = HTMLField('简介', blank=True)
    itime = models.DateTimeField('保存日期', default=timezone.now)
    ipraise = models.IntegerField('人气值', default=0)
    # < td > {{infor.updatetime | date: "Y-m-d H:i:s"}} < / td >
    itype = models.ForeignKey(TypeInfo, verbose_name='类型', on_delete=models.CASCADE, )
    iuser = models.ForeignKey('dp_user.UserInfo', verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.ititle

    class Meta:
        verbose_name = '图片详情'
        verbose_name_plural = '图片详情'
