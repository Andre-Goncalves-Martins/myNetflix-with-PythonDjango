from .models import Filme

def filmes_recentes(request):
    recent_films = Filme.objects.all().order_by('-data_criacao')
    return {"filmes_recentes" : recent_films}

def filmes_alta(request):
    film_em_alta = Filme.objects.all().order_by('-visualizacoes')
    return {"filmes_alta" : film_em_alta}

def filme_destaque(request):
    destaque = Filme.objects.order_by('-visualizacoes')[0] #Configurando como o filme mais visto
    #destaque = destaque.order_by('-data_criacao')
    return {"filme_destaque" : destaque}