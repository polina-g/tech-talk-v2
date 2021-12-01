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

        widget = {
            'user': form.TextInput(attrs={'class': 'form-control'}),
            'bio': form.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': form.TextInput(attrs={'class': 'form-control'}),
            'profile_background_pic': form.TextInput(attrs={'class': 'form-control'}),
            'website_url': form.TextInput(attrs={'class': 'form-control'}),
            'youtube_url': form.TextInput(attrs={'class': 'form-control'}),
            'github_url': form.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': form.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': form.TextInput(attrs={'class': 'form-control'}),

        }