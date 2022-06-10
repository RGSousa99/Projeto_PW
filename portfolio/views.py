import cloudinary.uploader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
    context = {'noticias': Noticia.objects.all()}
    return render(request, 'portfolio/pw.html', context)


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
        return render(request, 'portfolio/resultadosDoQuizz.html')

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
    plt.savefig('resultados.png', bbox_inches='tight')
    cloudinary.config(
        cloud_name="rgsousa99",
        api_key="764835177596756",
        api_secret="WRolP8_AJDKEUr7iAr02ybnP3iQ"
    )
    cloudinary.uploader.upload('resultados.png', public_id="portfolio/resultados", invalidate=True)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "portfolio/home.html")
        else:
            return render(request, "portfolio/login.html", {
                'message': "Cardenciais invalidas."
            })
    return render(request, "portfolio/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'portfolio/login.html', {
        "message": "Logged out."
    })

@login_required
def novo_projetos_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = ProjetoForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}
    return render(request, 'portfolio/novoProjeto.html', context)

@login_required
def view_editar_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'projeto_id': projeto_id}
    return render(request, 'portfolio/editaProjeto.html', context)

@login_required
def view_apagar_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

@login_required
def nova_cadeira_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form_c = CadeiraForm(request.POST or None)

    if form_c.is_valid():
        form_c.save()
        return HttpResponseRedirect(reverse('portfolio:apresentacao'))

    context = {'form': form_c}
    return render(request, 'portfolio/novaCadeira.html', context)

@login_required
def view_editar_cadeira(request, cadeira_id):
    cadeira = Cadeira.objects.get(id=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:apresentacao'))

    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/editaCadeira.html', context)

@login_required
def view_apagar_cadeira(request, cadeira_id):
    cadeira = Cadeira.objects.get(id=cadeira_id)
    cadeira.delete()
    return HttpResponseRedirect(reverse('portfolio:apresentacao'))


def resultados_page_view(request):
    return render(request, 'portfolio/resultadosDoQuizz.html')
