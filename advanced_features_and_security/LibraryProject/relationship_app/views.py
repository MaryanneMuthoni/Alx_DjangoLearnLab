from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required

# Create your views here.

def book_list(request):
    '''Lists all books stored in the database
    view should render a simple text list of book titles and their authors'''
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    '''displays details for a specific library, listing all books available in that library'''
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Add all books available in this library to the context."""
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Check if user is an Admin
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Check if user is a Librarian
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Check if user is a Member
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        publication_year = request.POST.get('publication_year')
        library_id = request.POST.get('library_id')

        author = get_object_or_404(Author, id=author_id)
        library = get_object_or_404(Library, id=library_id)

        Book.objects.create(
            title=title,
            author=author,
            publication_year=publication_year,
            library=library
        )
        return redirect('books')

    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('books')

    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('books')

    return render(request, 'relationship_app/delete_book.html', {'book': book})
