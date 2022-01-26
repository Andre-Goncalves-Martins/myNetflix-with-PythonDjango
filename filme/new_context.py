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

# def filmes_categoria(request):
#     film_acao = Filme.objects.filter(categoria= Filme.ge'acao')

#     return film_acao