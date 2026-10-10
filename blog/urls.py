from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users_list, name='users'),
    path('blogs/', views.posts_list, name='blogs'),
    path('comments/', views.comments_list, name='comments'),
    path('categories/', views.categories_list, name='categories'),
    path('blogs/<slug:slug>/', views.post_detail, name='post_detail'),
]