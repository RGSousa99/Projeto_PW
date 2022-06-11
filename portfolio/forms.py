from django import forms
from django.forms import ModelForm

from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'placeholder': 'Miguel Silva'}),
            'titulo': forms.TextInput(attrs={'placeholder': 'Projeto de programação'}),
            'descricao': forms.Textarea(attrs={'size': '150', 'width': '100%', 'rows': '5', 'wrap': 'soft',
                                               'maxlenght': '150', 'style': 'width: 95%'}),
            'data': forms.HiddenInput(),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'autor': 'Nome',
            'titulo': 'Título',
            'descricao': 'Descrição',
            'data': 'Data'
        }

    # texto auxiliar a um determinado campo do formulário
    help_texts = {
        'autor': 'indique o seu nome',
        'titulo': 'indique qual o projeto em que trabalhou comigo',
        'descricao': 'indique até 155 caracteres como foi a experiência'
    }

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {

            'titulo': forms.TextInput(attrs={'placeholder': 'Projeto de programação'}),
            'descricao': forms.Textarea(attrs={'size': '150', 'width': '100%', 'rows': '5', 'wrap': 'soft',
                                               'maxlenght': '150', 'style': 'width: 95%'}),

        }

        # texto a exibir junto à janela de inserção
        labels = {

            'titulo': 'Título',
            'descricao': 'Descrição'
        }

    # texto auxiliar a um determinado campo do formulário
    help_texts = {
        'titulo': 'indique qual o projeto em que trabalhou comigo',
        'descricao': 'indique até 155 caracteres como foi a experiência'
    }

class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {

            'titulo': forms.TextInput(attrs={'placeholder': 'Projeto de programação'}),
            'descricao': forms.Textarea(attrs={'size': '150', 'width': '100%', 'rows': '5', 'wrap': 'soft',
                                               'maxlenght': '150', 'style': 'width: 95%'}),

        }

        # texto a exibir junto à janela de inserção
        labels = {

            'titulo': 'Título',
            'descricao': 'Descrição',

        }

    # texto auxiliar a um determinado campo do formulário
    help_texts = {

        'titulo': 'indique qual o projeto em que trabalhou comigo',
        'descricao': 'indique até 155 caracteres como foi a experiência'
    }

class TfcForm(ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {

            'titulo': forms.TextInput(attrs={'placeholder': 'Projeto de programação'}),
            'resumo': forms.Textarea(attrs={'size': '150', 'width': '100%', 'rows': '5', 'wrap': 'soft',
                                               'maxlenght': '150', 'style': 'width: 95%'}),

        }

        # texto a exibir junto à janela de inserção
        labels = {

            'titulo': 'Título',
            'resumo': 'Descrição',

        }

    # texto auxiliar a um determinado campo do formulário
    help_texts = {

        'titulo': 'indique qual o projeto em que trabalhou comigo',
        'resumo': 'indique até 155 caracteres como foi a experiência'
    }