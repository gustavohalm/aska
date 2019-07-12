from django import forms
from . import models


class PartnerForm(forms.ModelForm):
    class Meta:
        model = models.Partner
        exclude = ['user']
        labels = {
            'name' : 'Nome',
            'cpf': 'CPF',
            'rg' : 'RG',
            'born': 'Data de Nascimento',
        }


class FarmForm(forms.ModelForm):
    class Meta:
        model = models.Farm
        exclude = ['user']
        labels = {
            'name': 'Nome da Fazenda',
            'insc_state': 'Inscrição Estadual'
        }


class PartnershipForm(forms.ModelForm):
    class Meta:
        model = models.Partnership
        exclude = ['farm']
        labels = {
            'partner': 'Sócio',
            'percent': 'Porcentagem',
        }


class BillForm(forms.ModelForm):
    class Meta:
        model = models.Bill
        exclude = ['user']
        labels = {
            'farm':'Fazenda',
            'type': 'Tipo',
            'bank_account:': 'Conta Bancaria',
            'account': 'Categoria',
            'provider': 'Fornecedor/Comprador',
            'description': 'Descrição',
            'date': 'Data'
        }
        widgets ={

            'farm': forms.Select(attrs= { 'class':'form-control forms'} ),
            'type': forms.Select(attrs= { 'class':'form-control forms'} ),
            'bank_account:': forms.Select(attrs= { 'class':'form-control forms'} ),
            'account': forms.Select(attrs= { 'class':'form-control forms'} ),
            'provider': forms.Select(attrs= { 'class':'form-control forms'} ),
            'description': forms.TextInput(attrs= { 'class':'form-control forms' } ),
            'date': forms.DateInput( attrs= { 'class':'form-control forms '})
        }