from rest_framework import serializers
from .models import Book, Author
from datetime import date
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    '''BookSerializer with custom validation for publication_year'''
    class Meta:
        model = Book
        fields = '__all__'

    #def validate(self, data):
    #    '''validate method overridden to ensure publication year is not in future'''
    #    current_year = timezone.now().year
    #
    #    if data['publication_year'] > current_year:
    #        raise serializers.ValidationError("Publication year must not be in future.")
    #    return data
    def validate(self, data):
        publication_year = data.get('publication_year')
        if publication_year:
            current_year = date.today().year
            # Compare the year part only
            if publication_year.year > current_year:
                raise serializers.ValidationError(
                    {"publication_year": "Publication year cannot be in the future."}
                )
        return data

class AuthorSerializer(serializers.ModelSerializer):
    '''AuthorSerializer with a books field that is a nested BookSerializer'''
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
