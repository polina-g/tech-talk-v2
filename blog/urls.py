from django.urls import path
from . import views

urls = [
path("", views.home, name = "home"),

]