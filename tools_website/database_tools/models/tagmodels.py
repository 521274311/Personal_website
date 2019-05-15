from django.db import models

class Tag(models.Model):
    TAG_STATUS_FIELDS = (
        (0, '未使用'),
        (1, '使用中'),
        (2, '已删除'),
    )

    tag_name = models.CharField(max_length=255, verbose_name='分类名')
    tag_status = models.SmallIntegerField(verbose_name=2, choices=TAG_STATUS_FIELDS, default=0)

    class Meta:
        app_label = 'database_tools'