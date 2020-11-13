from django import forms
from .models import Diary


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
