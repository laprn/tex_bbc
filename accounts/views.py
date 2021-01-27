# Create your views here.
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import EditProfileForm

from .models import CustomUser

class UserEditView(generic.UpdateView):
    model = CustomUser
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('diary:all_posts')

    def get_object(self):
        return self.request.user

