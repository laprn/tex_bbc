from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('password/', auth_views.PasswordChangeView.as_view()),
]
