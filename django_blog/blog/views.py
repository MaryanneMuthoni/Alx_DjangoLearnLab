from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.utils import timezone
from .forms import CustomUserCreationForm, PostForm, CommentForm

# Create your views here.
class SignUpView(CreateView):
    '''Handle user registration'''
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'

def profile(request):
    return render(request, 'profile.html')

@login_required
def profile_view(request):
    """
    Allows authenticated users to view and edit their profile details.
    Handles POST requests to update user information.
    """
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'blog/profile.html', {'form': form})

class BlogListView(ListView):
    '''display all blog posts'''
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list'

class BlogDetailView(DetailView):
    '''show individual blog posts'''
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class BlogCreateView(LoginRequiredMixin, CreateView):
    '''allow authenticated users to create new posts'''
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    '''enable post authors to edit their posts'''
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('list')
    context_object_name = 'post'

    def test_func(self):
        '''A test that the current logged-in user must pass to access the view- must be author'''
        post = self.get_object()
        return self.request.user == post.author

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''let authors delete their posts'''
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('list')

    def test_func(self):
        '''A test that the current logged-in user must pass to access the view- must be author'''
        post = self.get_object()
        return self.request.user == post.author


# Comment views
class CommentListView(ListView):
    '''display all comments under a blog posts'''
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comment_list'

class CommentDetailView(DetailView):
    '''show individual comments on blog posts'''
    model = Comment
    template_name = 'blog/comment_detail.html'
    context_object_name = 'comment'

class CommentCreateView(LoginRequiredMixin, CreateView):
    '''allow authenticated users to add new comments'''
    model = Comment
    form_class = CommentForm
    template_name = 'comment/comment_create.html'
    success_url = reverse_lazy('posts/comments')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.created_at = timezone.now()
        form.instance.updated_at = timezone.now()
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    '''enable users to edit their comments'''
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html'
    success_url = reverse_lazy('posts/comments')
    context_object_name = 'comment'

    def test_func(self):
        '''A test that the current logged-in user must pass to access the view- must be author'''
        post = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''let user delete their comment'''
    model = Comment
    template_name = 'blog/comment_delete.html'
    success_url = reverse_lazy('posts/comments')

    def test_func(self):
        '''A test that the current logged-in user must pass to access the view- must be author'''
        post = self.get_object()
        return self.request.user == comment.author
