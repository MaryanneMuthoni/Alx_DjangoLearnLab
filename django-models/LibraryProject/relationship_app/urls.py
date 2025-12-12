from django.urls import path
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path('list/', views.list_books, name='list'),
    path('library/', views.LibraryDetailView.as_view(), name='library'),
]
