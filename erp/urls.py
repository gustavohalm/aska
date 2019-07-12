from django.urls import path, include
from . import views
urlpatterns =[
    path('cadastro/socios/', views.PartnerCreateView.as_view(), name='partern_register'),
    path('create/farm/', views.FarmCreateView.as_view(), name='farm_create'),
    path('create/farm/<int:pk>/partnership/', views.partnershipCreateView, name='partnership_create'),
    path('bills/', views.billCreateView, name='bill_create')
]