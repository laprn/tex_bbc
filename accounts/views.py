# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm
from .models import CustomUser
from django.views.generic import DetailView
from diary.models import Profile


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class UserEditView(generic.UpdateView):
    model = CustomUser
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('diary:all_posts')

    def get_object(self):
        return self.request.user

