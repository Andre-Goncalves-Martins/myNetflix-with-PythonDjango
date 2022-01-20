from django.contrib import admin
from .models import Episodio, Filme

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)