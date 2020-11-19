from accounts.models import CustomUser
from django.db import models
from ckeditor.fields import RichTextField


class Diary(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='Title', max_length=40)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
        return self.title + '|' + str(self.user)


class Comment(models.Model):
    post = models.ForeignKey(Diary, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)



