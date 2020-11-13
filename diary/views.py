from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Diary


class IndexView(generic.TemplateView):
    template_name = 'index.html'


class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'

    def get_queryset(self):
        diaries = Diary.object.filter(user=self.request.user).order_by('-created-at')
        return diaries
