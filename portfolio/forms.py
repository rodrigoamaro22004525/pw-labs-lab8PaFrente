from django import forms
from .models import Comment
from .models import Programacao


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class ProgramacaoForm(forms.ModelForm):

    class Meta:
        model = Programacao
        fields = ['img', 'nomeDoProjeto']
