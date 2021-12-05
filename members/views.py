from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from members.models import Profile
from django.contrib.auth.models import User

def success(request):
    return render('authenticate/success.html')

# def profile(request):
#     return render(request, 'authenticate/profile.html')

def login_user(request):
    error_message = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/blogs/')
        else:
            error_message = 'Incorrect credentials. Please make sure all the information is entered correctly and try again.'
            return render(request, 'authenticate/login.html', {'error': error_message})
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/members/register/create_profile/')
        else:
            error_message = 'An unexpected error occured! Please make sure all the information is entered correctly and try again.'
    else:
        form = UserCreationForm()
    
    return render(request, 'authenticate/register_user.html', {'form': form,
    'error': error_message})

class ProfileCreate(CreateView):
    model = Profile
    fields = ('bio', 'profile_pic', 'profile_background_pic', 'website_url', 'youtube_url', 'github_url', 'linkedin_url', 'twitter_url')
    success_url = '/blogs/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileView(DetailView):
    model = Profile
    template_name = 'authenticate/profile.html'

class UserEditView(UpdateView):
    model = User
    template_name = 'authenticate/edit_user.html'
    def get_success_url(self):
        return f'/members/profile/{self.request.user.id}'
    fields = ('username', 'first_name', 'last_name', 'email')

    def get_object(self):
        return self.request.user


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'authenticate/edit_profile.html'
    fields = ('bio', 'profile_pic', 'profile_background_pic', 'website_url', 'youtube_url', 'github_url', 'linkedin_url', 'twitter_url')

  