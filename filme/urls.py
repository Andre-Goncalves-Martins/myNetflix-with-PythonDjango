#aqui é onde vamos criar as paginas para os filmes
# Configurando então os links onde vão estar

from unicodedata import name
from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhesfilme, Pesquisafilme

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilmes'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme')
]