from django.db import models
from django.db.models import manager


class Subtitle(models.Model):
    file_path = models.TextField(null=False, blank=False, unique=True, verbose_name='파일경로', )
    encoding_type = models.CharField(max_length=10, verbose_name='인코딩 타입', )

    objects = manager

    class Meta:
        db_table = 'subtitle'
        verbose_name = '자막'
        verbose_name_plural = '자목록록'
