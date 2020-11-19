# Create your views here.
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy


class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('all_posts')

