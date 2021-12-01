from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from django.db.models import fields
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from members.models import Profile
from .models import User


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'authenticate/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

def success(request):
    return render('authenticate/success.html')

def profile(request):
    return render(request, 'authenticate/profile.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/blogs/')
        else:
            return redirect('/members/login_user/')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/blogs/')
    else:
        form = UserCreationForm()
    
    return render(request, 'authenticate/register_user.html', {'form': form})

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'authenticate/edit_profile.html'
    success_url = ('/blogs/')

    def get_object(self):
        return self.request.user

  