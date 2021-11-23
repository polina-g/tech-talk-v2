from django.shortcuts import render
from django.views.generic.list import ListView
from .models import BlogEntry

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class BlogIndex(ListView):
    model = BlogEntry
    template_name = "blogs/index.html"