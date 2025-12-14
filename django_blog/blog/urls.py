from django.contrib import admin
from django.urls import path
from .views import SignUpView, profile_view, profile, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_view, name='profile_update'),
    path('posts/', BlogListView.as_view(), name='blog_list'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('post/new/', BlogCreateView.as_view(), name='blog_create'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
