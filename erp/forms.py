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

        widgets = {
            'name': forms.TextInput(attrs= { 'class':'form-control forms' } ),
            'cpf' :   forms.NumberInput( attrs= { 'class':'form-control forms'}),
            'rg':   forms.NumberInput( attrs= { 'class':'form-control forms'}),
            'born': forms.DateInput( attrs= { 'class':'form-control forms '})
        }


class FarmForm(forms.ModelForm):
    class Meta:
        model = models.Farm
        exclude = ['user']
        labels = {
            'name': 'Nome da Fazenda',
            'insc_state': 'Inscrição Estadual'
        }
        widgets= {
            'name': forms.TextInput(attrs= { 'class':'form-control forms' } ),
            'insc_state':  forms.NumberInput( attrs= { 'class':'form-control forms'})
        }


class PartnershipForm(forms.ModelForm):
    class Meta:
        model = models.Partnership
        exclude = ['farm']
        labels = {
            'partner': 'Sócio',
            'percent': 'Porcentagem',
        }

        widgets = {
                'partner': forms.Select(attrs= { 'class':'form-control forms' } ),
            'percent':  forms.NumberInput( attrs= { 'class':'form-control forms'})
        }

class BillForm(forms.ModelForm):
    class Meta:
        model = models.Bill
        exclude = ['user']
        labels = {
            'farm':'Fazenda',
            'type': 'Tipo',
            'bank_account': 'Conta Bancaria',
            'value': 'Valor',
            'account': 'Categoria',
            'provider': 'Fornecedor/Comprador',
            'description': 'Descrição',
            'date': 'Data'
        }
        widgets ={

            'farm': forms.Select(attrs= { 'class':'form-control forms'} ),
            'type': forms.Select(attrs= { 'class':'form-control forms'} ),
            'value': forms.NumberInput( attrs= { 'class':'form-control forms'}),
            'bank_account': forms.Select(attrs= { 'class':'form-control forms'} ),
            'account': forms.Select(attrs= { 'class':'form-control forms'} ),
            'provider': forms.Select(attrs= { 'class':'form-control forms'} ),
            'description': forms.TextInput(attrs= { 'class':'form-control forms' } ),
            'date': forms.DateInput( attrs= { 'class':'form-control forms '})
        }