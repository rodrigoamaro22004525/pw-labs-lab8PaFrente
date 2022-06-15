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
    gitLink = models.CharField(default="https://github.com/rodrigoamaro22004525", max_length=200)
    nome = models.CharField(max_length=50)
    linguagens = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.nome


class pontuacaoquizz(models.Model):
    name = models.CharField(User, max_length=50, blank=True)

    Q1 = models.CharField(null=True, max_length=200)
    Q2 = models.CharField(null=True, max_length=200)
    Q3 = models.CharField(null=True, max_length=200)
    Q4 = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name

    """
        Q1 -> Qual o animal que a google aluga para o seu uso (cabra)
        Q2 -> Quando foi inventado o Keyboard do estilo QWERTY (1868)
        Q3 -> De que material foi feito o primeiro rato (madeira)
        Q4 -> Qual foi o primeiro tweet da google? (I’m 01100110 01100101 01100101 01101100 01101001 01101110 01100111 00100000 01101100 01110101 01100011 01101011 01111001 00001010)
        """


class media(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Quizz/', blank=True)


class licenciatura(models.Model):
    nomeCadeira = models.CharField(max_length=50)
    semestre = models.IntegerField(default=1)
    etcs = models.IntegerField(default=0)
    link_cadeira = models.URLField(blank=True)
    rank = models.CharField(max_length=6)
    ano = models.IntegerField(default=1)
    """⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐"""

    def __str__(self):
        return self.nomeCadeira


# programação web
class noticias(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=300)
    img = models.ImageField(upload_to='media/', null=True)
    linkNot = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo


class tecnologias(models.Model):
    nome = models.CharField(max_length=50)
    acronimo = models.CharField(max_length=5)
    ano = models.DateTimeField(default=6 / 14 / 2022)
    autor = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='media/', null=True)
    linkYo = models.CharField(max_length=200, default="https://github.com/rodrigoamaro22004525?tab=repositories")
    descricao = models.CharField(max_length=400)

    def __str__(self):
        return self.nome

# programação web
