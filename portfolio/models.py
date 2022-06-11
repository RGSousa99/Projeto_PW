from django.db import models


# Create your models here.
import portfolio

class Post(models.Model):
    autor = models.CharField(max_length=20)
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo

class Professor(models.Model):
    nome = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Colega(models.Model):
    nome = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=200)
    pagAPP = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nome}"

class Cadeira(models.Model):
    nome = models.CharField(max_length=45)
    realizacao = models.CharField(max_length=9)
    topicos = models.CharField(max_length=500)
    pagCadeira = models.CharField(max_length=200)
    pofessor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ects = models.IntegerField()
    classicicacao = models.IntegerField()
    ano = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField()
    realizacao = models.DateField()
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    participantes = models.ForeignKey(Colega, on_delete=models.CASCADE)
    github = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)
    tecnologias = models.CharField(max_length=200)
    competencias = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=30)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=500)
    imagem = models.ImageField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class TFC(models.Model):
    autores = models.ForeignKey(Colega, on_delete=models.CASCADE)
    orientadores = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ano = models.CharField(max_length=5)
    titulo = models.CharField(max_length=50)
    resumo = models.CharField(max_length=500)
    imagem = models.ImageField()
    relatorio = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    video = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
