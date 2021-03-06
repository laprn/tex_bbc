from django import forms
from .models import Diary
from .models import Comment
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from accounts.models import CustomUser
from ckeditor.fields import RichTextField


class InquiryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label='Mail Address')
    title = forms.CharField(label='Title', max_length=30)
    message = forms.CharField(label='Content', widget=forms.Textarea)


class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'content')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
<<<<<<< HEAD
            #'name': forms.TextInput(),
            'body': forms.Textarea(),

=======
            # 'name': forms.TextInput(),
            'body': forms.TextInput(),
>>>>>>> 5883fa8d860596d552c4124634bb80a3730bab56
        }


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField(max_length=25, widget=forms.TextInput)
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'date_joined')

