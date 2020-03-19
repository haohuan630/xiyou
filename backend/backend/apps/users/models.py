from django.db import models


# Create your models here.


class Area(models.Model):
    """
    学院、专业、方向
    """
    name = models.CharField(max_length=20, verbose_name='名称')
    # 外键关联属性
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               related_name='subs',
                               null=True,
                               blank=True,
                               verbose_name='上级行政区划')

    class Meta:
        db_table = 'tb_areas'
        verbose_name = '行政区划'
        verbose_name_plural = '行政区划'

    def __str__(self):
        return self.name


class PersonInfo(models.Model):
    """
    人员信息表
    """
    name = models.CharField(max_length=20, verbose_name='姓名')
    url = models.CharField(null=True, max_length=300, verbose_name='详情链接')
    content = models.TextField(null=True, blank=True, verbose_name='人员详情')
    brief_intro = models.TextField(null=True, blank=True, verbose_name='人员简介')
    email = models.CharField(null=True, max_length=100, verbose_name='人员邮箱')
    views = models.CharField(null=True, max_length=20, verbose_name='浏览数')
    code = models.CharField(max_length=20, verbose_name='人员编码')
    sex = models.CharField(null=True, max_length=20, verbose_name='性別')
    main_fields = models.CharField(max_length=20, null=True, verbose_name='人员编码')

    areas = models.ManyToManyField(Area,
                                   db_table='tb_collect',
                                   verbose_name='专业和人员关联表')

    class Meta:
        db_table = 'tb_person'
        verbose_name = '人员信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
