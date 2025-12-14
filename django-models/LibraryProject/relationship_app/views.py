from django.shortcuts import render
from .models import Author
from .models import Book
from .models import Library
from .models import Librarian
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


# Create your views here.
def list_books(request):
    '''Lists all books stored in the database'''
    books = Book.objects.all()
    context= {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    '''Displays details for a specific library, listing all books available in that library'''
    model = Library
    template_name = 'relationship_app/library_detail.html'

class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def is_admin(user):
    '''Checks if user has a profile and is admin, returns True/False'''
    return hasattr(user, 'userprofile') and user.userprofile.role.lower() == 'admin'

def is_librarian(user):
    '''Checks if user has a profile and is librarian, returns True/False'''
    return hasattr(user, 'userprofile') and user.userprofile.role.lower() == 'librarian'

def is_member(user):
    '''Checks if user has a profile and is member, returns True/False'''
    return hasattr(user, 'userprofile') and user.userprofile.role.lower() == 'member'

@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    '''Renders view for user who is admin'''
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    '''Renders view for user who is librarian'''
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='login')
def member_view(request):
    '''Renders view for user who is member'''
    return render(request, 'relationship_app/member_view.html')
