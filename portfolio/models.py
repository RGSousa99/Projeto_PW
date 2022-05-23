from django.db import models


# Create your models here.
class Post(models.Model):
    autor = models.CharField(max_length=20)
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo

class Cadeira(models.Model):
    nome = models.CharField(max_length=45)
    realizacao = models.CharField(max_length=9)
    topicos = models.CharField(max_length=500)
    pagCadeira = models.CharField(max_length=200)
    pofessor = models.CharField(max_length=25)
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
    cadeira = Cadeira
    participantes = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    youtube = models.CharField(max_length=200)
    tecnologias = models.CharField(max_length=200)
    competencias = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
