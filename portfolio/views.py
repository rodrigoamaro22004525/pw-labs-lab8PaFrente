from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.conf import settings

from .forms import *
from .models import *

from .functions import desenha_grafico_resultados

from django.contrib import messages


# Create your views here.
def home_page_view(request):
    current_user = request.user
    user_id = current_user.id
    context = {'user_id': user_id}
    return render(request, 'portfolio/home.html', context)


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


#  blog
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
    post = Post.objects.get(slug=slug or None)

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
    projetos = {'programacao': Projetos.objects.all()}

    return render(request, 'portfolio/programacao.html', projetos)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('portfolio:home')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('portfolio:login')
        context = {
            'form': form,
        }
        return render(request, 'portfolio/register.html', context)


def login_page_view(request):
    if request.user.is_authenticated:
        return redirect('portfolio:home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'portfolio/login.html', context)


@login_required
def logoutPage(request):
    logout(request)
    return redirect('/')


def quizz_page_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Utilizador não efetuou login')

        return redirect('portfolio:home')
    else:
        form = PontuacaoQuizzForm(request.POST)
        user = User.objects.get(username=request.user.get_username())

        if request.method == 'POST':
            if form.is_valid():
                form = form.save(commit=False)
                form.name = user.username
                form.save()
                desenha_grafico_resultados(pontuacaoquizz.objects.all())
                form.save()
                return HttpResponseRedirect(request.path_info)

        else:
            context = {
                'form': form,
            }
            return render(request, 'portfolio/quizz.html', context)
