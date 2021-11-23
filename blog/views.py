from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogEntry

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class BlogIndex(ListView):
    model = BlogEntry
    template_name = "blogs/index.html"

    def get_queryset(self):
        queryset = BlogEntry.objects.filter()
        return queryset

# def blogs_index(request):
#     blogs = BlogEntry.objects.all()
#     return render(request, "blogs/index.html", {"blogs": blogs})