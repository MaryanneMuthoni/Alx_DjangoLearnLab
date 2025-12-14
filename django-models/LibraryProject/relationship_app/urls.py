from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import register
from .views import admin_view
from .views import librarian_view
from .views import member_view
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('signup/', views.register.as_view(template_name='relationship_app/register.html'), name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
