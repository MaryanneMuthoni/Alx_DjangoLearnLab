from django.contrib import admin
from django.urls import path
from .views import SignUpView, profile_view, profile, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CommentListView, CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView
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
    path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('posts/comments', CommentListView.as_view(), name='comment_list'),
    path('post/<int:pk>/comments', CommentDetailView.as_view(), name='comment_detail'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
