from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('password/', auth_views.PasswordChangeView.as_view(template_name='account/password_reset.html')),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
]
