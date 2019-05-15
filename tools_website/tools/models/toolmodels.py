from django.db import models
from django.contrib.auth.models import User
from .typemodels import Type
class Tool(models.Model):
    tool_link = models.CharField(max_length=255, verbose_name='工具连接')
    tag = models.OneToOneField(Type, on_delete=models.CASCADE, verbose_name='类别')
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    add_user = models.ForeignKey(User, verbose_name='创建管理员', on_delete=models.CASCADE)

    class Meta:
        app_label = 'tools'
        verbose_name = '工具链接'
