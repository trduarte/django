from django.forms import ModelForm
from django import forms
from site_1.models import Users

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Users
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha', 'nome', 'ultimo_nome']