from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
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


def blogs_detail(request, pk):
      blog = BlogEntry.objects.get(id = pk)

      return render(
          request,
          "blogs/detail.html", {
              "blog": blog
          }
      )

class BlogUpdate(UpdateView):
    model = BlogEntry
    success_url = "/blogs/"

class BlogDelete(DeleteView):
    model = BlogEntry
    # fields = ("title","blog_text", "date_posted", "image_url", "likes",)