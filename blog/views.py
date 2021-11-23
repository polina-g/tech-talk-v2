from django.shortcuts import render
from django.views.generic import ListView
# from django.views.generic.detail import DetailView
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

# def blogs_detail(request, pk):
#     blog = BlogEntry.objects.get(id = pk)
    
#     return render(
#          request,
#          "blogs/detail.html", {
#            "blog": blog, 
#          }


#     )

# class BlogDetail(DetailView):
#     model = BlogEntry
#     template_name = "deatil.html"