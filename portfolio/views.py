from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CommentForm
from .forms import ProgramacaoForm

from .models import Post
from portfolio.models import Programacao


# Create your views here.
def home_page_view(request):
    return render(request, 'portfolio/home.html')


# Create your views here.
def apresentacao_page_view(request):
    return render(request, 'portfolio/layout.html')


# Sobre
def sobre_page_view(request):
    return render(request, 'portfolio/sobre.html')


# Contacto
def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')


# Licenciatura
def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


# blog
def blog_page_view(request):
    posts = Post.objects.all()

    return render(request, 'portfolio/blog.html', {'posts': posts})


# virtualização
def virtualizacao_page_view(request):
    return render(request, 'portfolio/virtualizacao.html')


# Reverse-Eng
def reverse_page_view(request):
    return render(request, 'portfolio/reverse.html')


# detail
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST or None, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

        return redirect('portfolio:post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'portfolio/post_detail.html', {'post': post, 'form': form})


# projetos/programação
def programacao_page_view(request):
    projetos = {'programacao': Programacao.objects.all()}

    return render(request, 'portfolio/programacao.html', projetos)
