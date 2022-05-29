from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate


from .forms import *
from .models import *


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


def quizz_page_view(request):
    return render(request, 'portfolio/quizz.html')


def quizz(request):
    if request.method == 'POST':
        print(request.POST)
        perg = PontuacaoQuizz.objects.all()
        score = 0
        errado = 0
        certo = 0
        total = 0
        for q in perg:
            total += 1
            print(request.POST.get(q.pergunta))
            print(q.rep)
            print()
            if q.rep == request.POST.get(q.pergunta):
                score += 10
                certo += 1
            else:
                errado += 1
        porcento = score / (total * 10) * 100
        context = {
            'score': score,
            'correct': certo,
            'wrong': errado,
            'percent': porcento,
            'total': total
        }
        return render(request, 'portfolio/result.html', context)
    else:
        perg = PontuacaoQuizz.objects.all()
        context = {
            'perguntas': perg
        }
        return render(request, 'portfolio/home.html', context)


def addQuestion(request):
    if request.user.is_staff:
        form = PontuacaoQuizzForm()
        if request.method == 'POST':
            form = PontuacaoQuizzForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'portfolio/addQuestion.html', context)
    else:
        return redirect('portfolio:home')


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


def grafico_quiz_data(objects):
    data = {}
    for quizz in objects:
        data[quizz.nome] = PontuacaoQuizz(quizz)
        print(quizz.nome)

    return data


def grafico_quiz(objects):
    data = grafico_quiz_data(objects)
    users = list(data.keys())
    values = list(data.values())

    plt.bar(users, values, color='green', width=0.5)

    plt.xlabel("Jogadores")
    plt.ylabel("Pontuação")
    plt.title("Quiz Programação Web")
    plt.savefig('portfolio/static/portfolio/images/grafico.png')


def resultPage(request, nome):
    post = Post.objects.get(nome=nome or None)

    if request.method == 'POST':
        form = PontuacaoQuizzForm(request.POST or None, request.FILES)

        if form.is_valid():
            PontuacaoQuizz = form.save(commit=False)
            PontuacaoQuizz.post = post
            PontuacaoQuizz.save()

        return redirect('portfolio:quizz', nome=post.nome)
    else:
        form = PontuacaoQuizzForm()

    return render(request, 'portfolio/quizz.html', {'post': post, 'form': form})


