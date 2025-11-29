from django.contrib import admin
from .models import Book

# Customize the Admin Interface
# custom configurations to display title, author, and publication_year in the admin list view.
# Configure list filters and search capabilities to enhance the admin’s usability for Book entries.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register your models here.
admin.site.register(Book, BookAdmin)
