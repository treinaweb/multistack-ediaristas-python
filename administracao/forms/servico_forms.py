from django import forms
from django.forms import widgets
from ..models import Servico
from decimal import Decimal

class ServicoForm(forms.ModelForm):
    valor_minimo = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    porcentagem_comissao = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_quarto = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_sala = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_banheiro = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_quintal = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_cozinha = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
    valor_outros = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))

    class Meta:
        model = Servico
        fields = '__all__'


    def clean_valor_minimo(self):
        data = self.cleaned_data['valor_minimo']
        return Decimal(data.replace(',', '.'))

    def clean_porcentagem_comissao(self):
        data = self.cleaned_data['porcentagem_comissao']
        return Decimal(data.replace(',', '.'))

    def clean_valor_quarto(self):
        data = self.cleaned_data['valor_quarto']
        return Decimal(data.replace(',', '.'))

    def clean_valor_sala(self):
        data = self.cleaned_data['valor_sala']
        return Decimal(data.replace(',', '.'))

    def clean_valor_banheiro(self):
        data = self.cleaned_data['valor_banheiro']
        return Decimal(data.replace(',', '.'))

    def clean_valor_quintal(self):
        data = self.cleaned_data['valor_quintal']
        return Decimal(data.replace(',', '.'))

    def clean_valor_cozinha(self):
        data = self.cleaned_data['valor_cozinha']
        return Decimal(data.replace(',', '.'))

    def clean_valor_outros(self):
        data = self.cleaned_data['valor_outros']
        return Decimal(data.replace(',', '.'))

    