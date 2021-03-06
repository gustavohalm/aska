from django.urls import path, include
from . import views
from rest_framework import routers
from erp.api import viewsets

router = routers.DefaultRouter()
router.register('bills', viewsets.BillsViewset, base_name='bills_endpoint')
router.register('partner', viewsets.PartnerViewset, base_name='partner_endpoint')
router.register('partnership', viewsets.PartnershipViewset, base_name='partnership_endpoint')
router.register('farm', viewsets.FarmViewset, base_name='farm_endpoint')

urlpatterns = [
    path('', views.homeView, name='home'),
    path('cadastro/socios/', views.PartnerCreateView.as_view(), name='partner_create'),
    path('socios/', views.PartnerListView.as_view(), name='partner_list'),
    path('cadastro/fazendas/', views.FarmCreateView.as_view(), name='farm_create'),
    path('fazendas/', views.FarmListView.as_view(), name='farm_list'),
    path('cadastro/fazendas/<int:pk>/sociedade/', views.partnershipCreateView, name='partnership_create'),
    path('cadastro/conta/', views.BankAccountCreateView.as_view(), name='bank_create'),
    path('cadastro/categoria/', views.AccountCreateView.as_view(), name='account_create'),
    path('cadastro/fornecedor/', views.ProviderCreateView.as_view(), name='provider_create'),
    path('lancamentos/', views.billCreateView, name='bill_create'),
    path('lancamentos/xml/', views.importXmlBillView, name='bill_import_xml'),
    path('lancamentos/excel/', views.importExcelBillView, name='bill_import_excel'),
    path('lancamentos/edit/<int:pk>/', views.BillUpdateView.as_view(), name='bill_update'),
    path('lancamentos/relatorio/', views.reportBillsView, name='bills_report'),
    path('estoque/cadastro/', views.ProductCreateView.as_view(), name='product_create'),
    path('estoque/produtos/', views.ProductListView.as_view(), name='product_list'),
    path('login/', views.loginView, name='login_view'),
    path('logout/', views.logoutView, name='logout_view'),
    path('api/v0/', include(router.urls))
]
