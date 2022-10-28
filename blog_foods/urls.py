from django.contrib.auth import login
from django.urls import path
from .views import AddPostView,DeletePostView,UpdatePostView
from . import views

app_name = 'blog_foods'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('create/', AddPostView.as_view(), name='create'),
    path('accounts/register/', views.register, name='register'),
    path('post/<int:pk>/', views.post, name='post'),
    path('author/<int:id>', views.author, name='author'),
    path('profile/', views.profile, name='profile'),
    path('upload-profile/', views.upload_profile, name='upload_profile'),
    path('post/<int:pk>/remove',DeletePostView.as_view(),name='delete_post'),
    path('post/edit/<int:pk>',UpdatePostView.as_view(),name='update_post')
]
