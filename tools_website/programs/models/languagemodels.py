from django.db import models


class Language(models.Model):
    NAME_FIELDS = (
        ('python', 'Python'),
        ('java', 'JAVA'),
        ('go', 'GO'),
        ('js', 'JS'),
        ('c', 'C'),
        ('c++', 'C++'),
        ('gcc', 'GCC'),
        ('r', 'R'),

    )
    STATUS_FIELD = (
        (0, '未使用'),
        (1, '正在使用'),
        (2, '已删除'),
    )

    name = models.CharField(max_length=50, verbose_name='语言名称', choices=NAME_FIELDS)
    version = models.CharField(max_length=10, verbose_name='语言版本')
    status = models.SmallIntegerField(verbose_name='语言状态', choices=STATUS_FIELD)

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    # add_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '编程语言'
        # unique_together = ('name', 'version')

    def __str__(self):
        return self.name+str(self.version)