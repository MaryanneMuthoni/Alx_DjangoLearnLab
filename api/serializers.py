from rest_framework import serializers
from .models import Book, Author
from datetime import datetime
from django.utils import timezone

class BookSerializer(serilizers.ModelSerializer):
    '''BookSerializer with custom validation for publication_year'''
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        '''validate method overridden to ensure publication year is not in future'''
        current_year = timezone.now().year

        if data['publication_year'] > current_year:
            raise serializers.ValidationError("Publication year must not be in future.")
        return data

class AuthorSerializer(serilizers.ModelSerializer):
    '''AuthorSerializer with a books field that is a nested BookSerializer'''
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
