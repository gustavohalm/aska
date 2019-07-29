from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from . import models, forms
from django.contrib.auth import authenticate, login
import xml.etree.ElementTree as ET
import  xlrd

def loginView(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../lancamentos/')

    return render(request, 'erp/login.html')

def logoutView(request):
    pass

class PartnerCreateView(CreateView):
    model = models.Partner
    form_class = forms.PartnerForm
    template_name = 'erp/partner_create.html'

    def post(self, request, *args, **kwargs):
        form = forms.PartnerForm(request.POST)
        if form.is_valid():
            partner = form.save(commit=False)
            partner.user = request.user
            partner.save()


#Creation of Farm's and their Owner's Partnership's
class FarmCreateView(CreateView):
    model = models.Farm
    form_class = forms.FarmForm
    template_name = 'erp/farm_create.html'

    def post(self, request, *args, **kwargs):
        form = forms.FarmForm(request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.user = request.user
            farm.save()
            return redirect('partnership_create', pk=farm.id)



def partnershipCreateView(request, pk):
    farm = models.Farm.objects.get(id=pk)

    if request.method == 'POST':
        form = forms.PartnershipForm(request.POST)
        partnership = form.save(commit=False)
        partnership.farm = farm
        partnership.save()
    if farm.get_partnership():
        partnership = farm.get_partnership()
        total = 0.0
        for i in partnership:
           total += float(i.percent)
        if total < 100:
            form = forms.PartnershipForm
        else:
            form = ''
    else:
        form = forms.PartnershipForm

    context = {
        'farm': farm,
        'form': form
    }
    return render(request, 'erp/partnership_create.html', context=context)


def billCreateView(request):
    if request.method == 'POST':

        form = forms.BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.user = request.user
            bill.save()

    bills = models.Bill.objects.filter(user=request.user)
    total = 0.00
    for bill in bills:
        if bill.type == 'Pagar':
            total -= float(bill.value)
        else:
            total += float(bill.value)

    form = forms.BillForm
    farms_options = models.Farm.objects.filter(user=request.user)
    bank_account_options = models.BankAccount.objects.filter(user=request.user)
    account_options = models.Account.objects.filter(user=request.user)
    provider_options = models.Provider.objects.filter(user=request.user)
    context = {
        'bills': bills,
        'form': form,
        'farms': farms_options,
        'bank_accounts': bank_account_options,
        'accounts': account_options,
        'providers': provider_options,
        'value_total': total,
    }

    return render(request, 'erp/bill_create.html', context=context)


class BillUpdateView(UpdateView):
    model = models.Bill
    success_url = '../..'
    form_class = forms.BillForm
    template_name = 'erp/bill_update.html'


def importExcelBillView(request):
    farms = models.Farm.objects.filter(user=request.user)
    import_bills = []
    if request.methode == 'POST':
        farm = request.POST['farm']
        file_excel = request.FILES['file']
        planilha = xlrd.open_workbook(file_excel)
        sheet = planilha.get_sheet(0)
        for row in range(0, sheet.nrows):
            date = sheet.cell(row, 0).value
            description = sheet.cell(row, 1).value
            provider = sheet.cell(row, 2).value
            
    context = {
        'farms': farms,
        'import_bills': import_bills,
    }
    return render(request, 'erp/import_excel.html', context)


def importXmlBillView(request):
    farms = models.Farm.objects.filter(user=request.user)
    xml = ''
    cnpj = ''
    if request.method == 'POST':
        farm = request.POST['farm']
        file_xml = request.FILES['file']
        xml = ET.parse(file_xml)
        elements = xml.getroot()
    context = {
        'farms': farms,
        'xml': xml,
        'cnpj': ''
    }
    return render(request, 'erp/import_xml.html', context)


def confirmImport(request):
    pass


def reportBillsView(request):

    if 'farm' in request.GET:
        farm = request.GET['farm']
        if 'year' in request.GET:
            year = request.GET['year']
            if 'month' in request.GET:
                month = request.GET['month']
                bills = models.Bill.objects.filter(farm=farm).filter(date__year=year).filter(date__month=month)
            else:
                bills = models.Bill.objects.filter(farm=farm).filter(date__year=year)
        else:
            bills = models.Bill.objects.filter(farm=farm)
    elif 'year' in request.GET:
        year = request.GET['year']
        if 'month' in request.GET:
            month = request.GET['month']
            bills = models.Bill.objects.filter(date__year=year).filter(date__month=month)
        else:
            bills = models.Bill.objects.filter(date__year=year)
    else:
        bills = []

    form = forms.BillForm
    context = {
        'form': form,
        'bills' : bills
        }
    return render(request, 'erp/report_bills.html', context)


class AccountCreateView(CreateView):
    model = models.Account
    success_url = '../..'
    form_class = forms.AccountForm
    template_name = 'erp/account_create.html'


class BankAccountCreateView(CreateView):
    model = models.BankAccount
    success_url = '../..'
    form_class = forms.BankAccountForm
    template_name = 'erp/bank_account_create.html'


class ProviderCreateView(CreateView):
    model = models.Provider
    success_url = '/'
    form_class =  forms.ProviderForm
    template_name = 'erp/provider_create.html'


