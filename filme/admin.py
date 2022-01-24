from django.contrib import admin
from .models import Episodio, Filme, Usuario
from django.contrib.auth.admin import UserAdmin

#Campo personalizado dentro de usuários para os filmes vistos
ADICIONAR_CAMPOS = list(UserAdmin.fieldsets)
ADICIONAR_CAMPOS.append(
    ('Histórico', {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(ADICIONAR_CAMPOS)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)