from django.shortcuts import render, redirect
from .models import Author
from .models import Book
from .models import Library
from .models import Librarian
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})

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

@method_decorator(permission_required('relationship_app.can_add_book', login_url='login'), name='dispatch')
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    success_url = '/books/'

@method_decorator(permission_required('relationship_app.can_change_book', login_url='login'), name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    success_url = '/books/'

@method_decorator(permission_required('relationship_app.can_delete_book', login_url='login'), name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = '/books/'
