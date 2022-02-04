#aqui é onde vamos criar as paginas para os filmes
# Configurando então os links onde vão estar
from unicodedata import name
from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhesfilme, Perfil, Pesquisafilme, Criarconta
from django.contrib.auth import views as auth_view


app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilmes'),
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name= 'login.html') , name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name= 'logout.html') , name='logout'),
    path('editarPerfil/', Perfil.as_view() , name='editarperfil'),
    path('criarconta/', Criarconta.as_view() , name='criarconta'),
]