from django.contrib import admin
from django.urls import path
from .views import SignUpView, profile_view, ProfileUpdateView 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_view, name='profile_update'),
]
