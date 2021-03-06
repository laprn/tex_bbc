from accounts.models import CustomUser
from django.db import models
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User


class Diary(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='Title', max_length=40)
    content = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='blog_posts')

    class Meta:
        verbose_name_plural = 'Diary'

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.user)


class Comment(models.Model):
    post = models.ForeignKey(Diary, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = RichTextField(extra_plugins=['mathjax'],)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)
