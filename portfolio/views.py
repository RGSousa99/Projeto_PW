from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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

def site_page_view(request):
    return render(request, 'portfolio/site.html')
