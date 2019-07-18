from rest_framework import viewsets
from . import  serializers
from erp import models

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


