from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse


class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    blog_text = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    image_url = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog_urls:index')

class Comment(models.Model):
    # foreign key connects comment model with post model related_name allows to grab it as "comment", automatically adds date to post without person adding it manually 
    blogentry = models.ForeignKey(BlogEntry, related_name="comments", on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.blogentry.title, self.username)

