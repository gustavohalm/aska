from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . import serializers
from erp import models


class PartnerViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PartnerSerializer

    def get_queryset(self):
        return models.Partner.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FarmViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.FarmSerialiazer

    def get_queryset(self):
        return models.Farm.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PartnershipViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.PartnershipSerialiazer

    def get_queryset(self):
        return models.Partnership.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BillsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.BillSerializer

    def get_queryset(self):
        if 'farm' in self.request.GET:
            farm = self.request.GET['farm']
            if 'year' in self.request.GET:
                if 'month' in self.request.GET:
                    return models.Bill.objects.filter(user=self.request.user,farm=farm, date__year=self.request.GET['year']).filter(date__month=self.request.GET['month'])
                return models.Bill.objects.filter(user=self.request.user, farm=farm,date__year=self.request.GET['year'])

        return models.Bill.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


