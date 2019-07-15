from django.urls import path, include
from . import views
urlpatterns =[
    path('cadastro/socios/', views.PartnerCreateView.as_view(), name='partner_create'),
    path('cadastro/fazendas/', views.FarmCreateView.as_view(), name='farm_create'),
    path('cadastro/fazendas/<int:pk>/sociedade/', views.partnershipCreateView, name='partnership_create'),
    path('lancamentos/', views.billCreateView, name='bill_create'),
    path('lancamentos/edit/<int:pk>', views.BillUpdateView.as_view(), name='bill_update')

]