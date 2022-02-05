import email
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class CriarContaForm(UserCreationForm):
    email = forms.EmailField(required=True)#require True para que seja obrigado receber o email

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')