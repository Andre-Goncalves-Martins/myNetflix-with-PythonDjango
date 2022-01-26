from dataclasses import field
from .models import Filme

def filmes_recentes(request):
    recent_films = Filme.objects.all().order_by('-data_criacao')
    return {"filmes_recentes" : recent_films}

def filmes_alta(request):
    film_em_alta = Filme.objects.all().order_by('-visualizacoes')
    return {"filmes_alta" : film_em_alta}

def filme_destaque(request):
    if Filme.objects.all().order_by('-visualizacoes'):
        destaque = Filme.objects.order_by('-visualizacoes')[0] #Configurando como o filme mais visto
    else:
        destaque = None
    return {"filme_destaque" : destaque}
    #destaque = destaque.order_by('-data_criacao')

def filmes_categoria(request):
    acao = Filme.objects.filter(categoria='acao')
    comedia = Filme.objects.filter(categoria='comedia')
    terror = Filme.objects.filter(categoria='terror')
    ficcao = Filme.objects.filter(categoria='ficcao')
    
    return {'filmes_acao' : acao, 'filmes_comedia' : comedia, 'filmes_terror' : terror, 'filmes_ficcao' : ficcao}