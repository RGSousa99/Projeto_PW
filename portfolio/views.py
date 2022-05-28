from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from matplotlib import pyplot as plt
from .forms import *
from .models import *
import datetime


def home_page_view(request):
    return render(request, 'portfolio/home.html')


def apresentacao_page_view(request):
    context = {'cadeiras': Cadeira.objects.all()}
    return render(request, 'portfolio/apresentacao.html', context)


def projetos_page_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)


def pw_page_view(request):
    return render(request, 'portfolio/pw.html')


def blog_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def novo_post_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/novoPost.html', context)


def quizz_page_view(request):
    if request.method == 'POST':
        n = request.POST['name']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
        desenha_grafico_resultados(request)

    return render(request, 'portfolio/quizz.html')

def pontuacao_quizz(request):
    score = 0
    if request.POST['pergunta1'] == "< p >":
        score += 1
    if request.POST['pergunta2'] == "z-index":
        score += 1
    if request.POST['pergunta3'] == "< dl >":
        score += 1
    if request.POST['pergunta4'] == "makemigrations":
        score += 1
    if request.POST['pergunta4.1'] == "migrate":
        score += 1
    if request.POST['pergunta5'] == ".css":
        score += 1
    return score

def desenha_grafico_resultados(request):
    nomes = []
    pontuacoes = []
    for score in PontuacaoQuizz.objects.all():
        nomes.append(score.nome)
        pontuacoes.append(score.pontuacao)
        nomes.reverse()
        pontuacoes.reverse()
        plt.barh(nomes, pontuacoes)
        plt.savefig('portfolio/static/portfolio/images/resultadoGrafico.png', bbox_inches='tight')
