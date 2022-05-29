from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=8, primary_key=True)


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(None)
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


class Projetos(models.Model):
    nome = models.CharField(max_length=50)
    linguagens = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.nome


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    pergunta_1 = models.CharField(null=True, max_length=200)
    pergunta_2 = models.CharField(null=True, max_length=200)
    pergunta_3 = models.CharField(null=True, max_length=200)
    pergunta_4 = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.nome



