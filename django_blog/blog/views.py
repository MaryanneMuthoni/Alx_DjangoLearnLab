from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.
class SignUpView(CreateView):
    '''Handle user registration'''
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'

def profile_view(request):
    return render(request, 'profile.html')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'blog/profile_update.html'
    success_url = 'profile'

    def get_object(self):
        return self.request.user
