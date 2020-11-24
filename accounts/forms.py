from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username')

