from .models import Filme

def filmes_recentes(request):
    recent_films = Filme.objects.all().order_by('-data_criacao')
    return {"filmes_recentes" : recent_films}

def filmes_alta(request):
    film_em_alta = Filme.objects.all().order_by('-visualizacoes')
    return {"filmes_alta" : film_em_alta}