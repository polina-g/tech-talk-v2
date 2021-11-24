from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    blog_text = models.TextField()
    date_posted = models.DateField()
    image_url = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    comment_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    blog_entry = models.ForeignKey(BlogEntry, on_delete=CASCADE)

    def __str__(self):
        return f'comment {self.comment_text} by {self.user.name}'
        




