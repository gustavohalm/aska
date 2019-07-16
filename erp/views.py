from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from . import models, forms


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
    context = {
        'bills': bills,
        'form': form,
        'value_total': total,
    }

    return render(request, 'erp/bill_create.html', context=context)


class BillUpdateView(UpdateView):
    model = models.Bill
    success_url = '../..'
    form_class = forms.BillForm
    template_name = 'erp/bill_update.html'


def importExcelBillView(request):
    pass


def importXmlBillView(request):
    pass


def relatorioBillsView8(request):
    pass