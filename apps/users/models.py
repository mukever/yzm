from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', blank=True, null=True)
    birthday = models.DateField(verbose_name=u'生日', blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name=u'地址', blank=True, null=True)
    age = models.IntegerField(verbose_name=u'年龄', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('Female', u'女'), ('Male', '男')), verbose_name=u'性别',
                              default='Male')
    image = models.ImageField(upload_to='images/%Y/%m', verbose_name=u'头像')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

