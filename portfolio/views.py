from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home_page_view(request):
    return render(request, 'portfolio/home.html')

def apresentacao_page_view(request):
    return render(request, 'portfolio/apresentacao.html')

def projetos_page_view(request):
    return render(request, 'portfolio/projetos.html')

def pw_page_view(request):
    return render(request, 'portfolio/pw.html')

def blog_page_view(request):
    return render(request, 'portfolio/blog.html')

def site_page_view(request):
    return render(request, 'portfolio/site.html')
