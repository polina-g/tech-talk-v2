from django.urls import path
from . import views

app_name = 'blog_urls'
urlpatterns = [
path("", views.home, name = "home"),
path("about/", views.about, name = "about"),
path("blogs/", views.BlogIndex.as_view(), name = "index"),
path("blogs/create", views.BlogCreate.as_view(), name = "blog_create"),
path("blogs/<int:pk>/", views.blogs_detail, name = "detail"),
path("blogs/<int:pk>/delete", views.BlogDelete.as_view(), name = "blog_delete"),

]