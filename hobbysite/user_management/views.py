from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegistrationForm, ProfileUpdateForm
from .models import Profile

class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "user_management/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        return redirect(self.success_url)
    

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "user_management/profile_update.html"
    success_url = reverse_lazy("homepage:home")


    def get_object(self, queryset=None):
        return self.request.user.profile