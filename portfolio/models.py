from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=8, primary_key=True)


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio_post')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


