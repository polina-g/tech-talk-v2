from django.urls import path

from . import views
urlpatterns = [
    # we will define all app-level urls in this list
    path('', views.home, name='home'),
]