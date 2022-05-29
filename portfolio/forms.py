from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
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
class ProjetosForm(forms.ModelForm):
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


class PontuacaoQuizzForm(forms.ModelForm):
    class Meta:
        model = pontuacaoquizz
        fields = ['Q1','Q2','Q3','Q4']

        """
            Q1 -> Qual o animal que a google aluga para o seu uso (cabra)
            Q2 -> Quando foi inventado o Keyboard do estilo QWERTY (1868)
            Q3 -> De que material foi feito o primeiro rato (madeira)
            Q4 -> Qual foi o primeiro tweet da google? (I’m 01100110 01100101 01100101 01101100 01101001 01101110 01100111 00100000 01101100 01110101 01100011 01101011 01111001 00001010)
        """

        widgets = {
            'Q1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Q1'}),
            'Q2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Q2'}),
            'Q3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Q3'}),
            'Q4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Q4'}),
        }

        labels = {
            'Q1': 'Qual o animal que a google aluga para o seu uso?',
            'Q2': 'Quando foi inventado o Keyboard do estilo QWERTY?',
            'Q3': 'De que material foi feito o primeiro rato?',
            'Q4': 'Qual foi o primeiro tweet da google?',
        }
