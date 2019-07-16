from rest_framework import viewsets
from . import  serializers
from erp import models

class BillsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.BillSerializer

    def get_queryset(self):
        return models.Bill.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


