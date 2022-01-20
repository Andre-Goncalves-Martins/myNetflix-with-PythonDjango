from django.db import models
from django.utils import timezone
# Create your models here.

#Lista de categorias para termos as opções lá no site
LISTA_CATEGORIAS = (
    #primeiro campo é o armazenado no bd e o segundo é o q aparece pra o usuário
    ('acao','Ação'),
    ('comedia','Comédia'),
    ('terror','Terror'),
    ('ficcao','Ficção Científica'),
)

#Cria o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15,choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.titulo

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self) -> str:
         return self.titulo