from django.db import models
from tinymce.models import HTMLField

class UserInfo(models.Model):
    uname = models.CharField('账号', max_length=20)
    unickname = models.CharField('用户名', max_length=50, default='')
    upwd = models.CharField('密码', max_length=40)
    uemail = models.CharField('邮箱', max_length=30)
    uintro = HTMLField('简介', max_length=300, default='', blank=True)
    uaddress = models.CharField('地址', max_length=100, default='', blank=True)
    uphone = models.CharField('手机号码', max_length=11, default='', blank=True)
    utime = models.DateTimeField('注册日期', auto_now_add=True)

    def __str__(self):
        return self.unickname

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'
