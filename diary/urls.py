from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('diary-list/', views.DiaryListView.as_view(), name='diary_list'),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),
    path('diary-create/', views.DiaryCreateView.as_view(), name='diary_create'),
    path('diary-update/<int:pk>', views.DiaryUpdateView.as_view(), name='diary_update'),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name='diary_delete'),
    path('all-posts/', views.AllPosts.as_view(), name='all_posts'),
    path('diary-detail/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    # path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view()),

    path('like/<int:pk>', views.LikeView, name='like_post'),
]
