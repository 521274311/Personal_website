from django.db import models
from django.contrib.auth.models import User

class Type(models.Model):
    TYPE_STATUS_WAIT = 0
    TYPE_STATUS_NORMAL = 1
    TYPE_STATUS_DEL = 2
    TYPE_STATUS_FIELD = (
        (TYPE_STATUS_WAIT, '未使用'),
        (TYPE_STATUS_NORMAL, '已使用'),
        (TYPE_STATUS_DEL, '已删除'),
    )

    name = models.CharField(max_length=100, verbose_name='类别名')
    parent = models.ForeignKey('self', verbose_name='上级类别', blank=True, null=True)
    status = models.SmallIntegerField(max_length=2, verbose_name='类别状态', choices=TYPE_STATUS_FIELD)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    add_user = models.ForeignKey(User, verbose_name='创建管理员')

    class Meta:
        app_label = 'tools'
        verbose_name = '工具类别'