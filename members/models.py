from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    bio = models.TextField()
    profile_pic = models.CharField(max_length=255, default="/static/images/default_profile_pic.jpeg",)
    profile_background_pic = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('members_urls:profile', kwargs={'pk': self.id})

# Added User methods

def get_user_id(self):
    return f'{self.id}'

def get_userprofile_id(self):
    return f'{self.profile.id}'

User.add_to_class("get_user_id", get_user_id)
User.add_to_class("get_userprofile_id", get_userprofile_id)