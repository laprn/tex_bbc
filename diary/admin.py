from django.contrib import admin
from .models import Diary, Comment, Profile

admin.site.register(Diary)
admin.site.register(Comment)
admin.site.register(Profile)
