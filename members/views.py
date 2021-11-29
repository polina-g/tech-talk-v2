from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields

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

    
    # 'form':form,
    # })
  
    


    #  successful registering message: messages.success(request, ("Registration was successful"))

# Create your views here.
            # messages.success(request, ("There was an error loging in, please try again") )


            #this is the logout button  messages.success(request, ("You were successfully logged out!") )