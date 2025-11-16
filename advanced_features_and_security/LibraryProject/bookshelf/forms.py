from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Book Title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author Name'}),
            'publication_year': forms.NumberInput(attrs={'placeholder': 'Publication Year'}),
        }
