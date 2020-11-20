from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField(max_length=25, widget=forms.TextInput)
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'date_joined')

