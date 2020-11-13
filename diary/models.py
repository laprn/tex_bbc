from accounts.models import CustomUser
from django.db import models


class Diary(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='コンテンツ', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
        return self.title
