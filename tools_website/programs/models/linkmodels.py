from .languagemodels import Language
from django.db import models

class Link(models.Model):
    STATUS_FIELD = (
        (0, '未使用'),
        (1, '正在使用'),
        (2, '已删除'),
    )

    l_language = models.OneToOneField(Language, on_delete=models.CASCADE, verbose_name='编程语言')
    url = models.TextField(verbose_name='链接')
    status = models.SmallIntegerField(verbose_name='状态', choices=STATUS_FIELD)

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    # add_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '链接'
        # unique_together = ('name', 'version')

    def __str__(self):
        return self.url