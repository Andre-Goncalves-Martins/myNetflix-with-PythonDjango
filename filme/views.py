from django.shortcuts import redirect
from . models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Homepage(TemplateView): #TemplateView é usada quando vc quer somente apresentar um template html
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)#redireciona para a homepage

class Homefilmes(LoginRequiredMixin, ListView): #ListView vai passar uma lista de todos os objetos q eu quiser do meu banco de dados dentro de um object_list
                            #Observe como está implementado no homefilmes.html   
    template_name = 'homefilmes.html'
    model = Filme
    #object_list -> lista de itens do modelo

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilmes.html'
    model = Filme
    #object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1        
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme) #Adicionando filme num campo do banco de dados
        return super().get(request, *args, **kwargs) # redireciona o user para url do filme selecionado
    
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        filmes_relacionados =  Filme.objects.filter(categoria=self.get_object().categoria)#caso queira limitar o numero pego pelo filtro, basta dar um slice, por exemplo [:3] para pegar os 3 primeiros da lista       
        context['filmes_relacionados'] = filmes_relacionados
        return context

class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        texto_pesquisa = self.request.GET.get('query')
        if texto_pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=texto_pesquisa)
            return object_list
        else:
            return super().get_queryset()
        
class Perfil(LoginRequiredMixin, TemplateView):
    template_name= 'editarperfil.html'
    

#Estrutura se fosse fuction based views

#def homepage(request):
#    return render(request, 'homepage.html')

#def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html',context)    