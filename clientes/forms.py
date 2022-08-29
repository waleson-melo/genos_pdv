from django import forms

from .models import Cliente


class CadastrarForm(forms.ModelForm):
    data_cadastro = forms.CharField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = Cliente
        fields = [
            'cpf',
            'nome',
            'telefone',
            'email',
        ]
