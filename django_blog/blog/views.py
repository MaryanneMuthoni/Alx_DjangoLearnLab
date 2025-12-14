from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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
