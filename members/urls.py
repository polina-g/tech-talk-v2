from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'members_urls'
urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name="register_user"),
    path('register/create_profile/', views.ProfileCreate.as_view(), name="create_profile"),
    path('edit/user/', views.UserEditView.as_view(), name='edit_user'),
    path('edit/<int:pk>/profile/', views.ProfileEditView.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='authenticate/change-password.html')),
    path('profile/<int:pk>', views.ProfileView.as_view(), name="profile"),
    ]
