from django import forms
from django.forms import ModelForm
from .models import User
from .models import Profile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ('user', 'bio', 'profile_pic', 'profile_background_pic', 'website_url', 'youtube_url', 'github_url', 'linkedin_url', 'twitter_url')
