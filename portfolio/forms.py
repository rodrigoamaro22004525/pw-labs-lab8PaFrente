from django import forms
from .models import Comment
from .models import Projetos


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


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