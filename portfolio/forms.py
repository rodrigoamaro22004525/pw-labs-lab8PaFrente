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
