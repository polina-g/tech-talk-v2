from django.urls import path
from . import views
from .views import UserEditView, ShowProfilePageView
from django.contrib.auth import views as auth_views


app_name = 'members_urls'
urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name="register_user"),
    path('edit_profile/', views.UserEditView.as_view(), name="edit_profile"),
    path('edit_profile/success/', views.UserEditView.as_view(), name="success"),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='authenticate/change-password.html')),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile_page"),
    

    ]
