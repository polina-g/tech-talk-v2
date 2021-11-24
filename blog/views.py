from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import BlogEntry

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#Blog Voews:
class BlogIndex(ListView):
    model = BlogEntry
    template_name = "blogs/index.html"

    def get_queryset(self):
        queryset = BlogEntry.objects.filter()
        return queryset

class BlogCreate(CreateView):
    model = BlogEntry
    fields = ('title', 'blog_text', 'image_url')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
