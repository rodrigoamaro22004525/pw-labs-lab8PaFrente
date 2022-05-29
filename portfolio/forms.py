from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Autor'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email do Autor'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'comentário do Autor'}),
        }

        labels = {
            'name': 'Name',
            'email': 'Email',
            'body': 'Body',
        }


# codigo inutil
class ProjetosForm(ModelForm):
    class Meta:
        model = Projetos
        fields = '__all__'

        # ferramentas
        widgets = {

        }

        help_texts = {

        }

        labels = {

            'nome': 'Insira o nome',
            'data': 'Data',
            'imagem': 'Insira a sua imagem',

        }


# codigo inutil

class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
        }

        labels = {
            'username': 'Username',
            'password': 'Password',
        }


class PontuacaoQuizzForm(ModelForm):
    class Meta:
        model = PontuacaoQuizz
        fields = "__all__"

        """
            Pergunta_1 -> Qual o animal que a google aluga para o seu uso (cabra)
            Pergunta_2 -> Quando foi inventado o Keyboard do estilo QWERTY (1868)
            Pergunta_3 -> De que material foi feito o primeiro rato (madeira)
            Pergunta_4 -> Qual foi o primeiro tweet da google? (I’m 01100110 01100101 01100101 01101100 01101001 01101110 01100111 00100000 01101100 01110101 01100011 01101011 01111001 00001010)
        """
        labels = {
            'nome': 'Nome',
            'Pergunta_1': 'Qual o animal que a google aluga para o seu uso',
            'Pergunta_2': 'Quando foi inventado o Keyboard do estilo QWERTY',
            'Pergunta_3': 'De que material foi feito o primeiro rato',
            'Pergunta_4': 'Qual foi o primeiro tweet da google?',
        }

        help_texts = {}
