from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication] #Token authentication
    #Grants permissions to Authenticated and admin to handle common CRUD operations
    permission_classes = [IsAuthenticated, IsAdminUser] 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
