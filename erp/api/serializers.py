from rest_framework import serializers
from erp import  models


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bill
        fields = '__all__'
        read_only_fields = ['id', 'user']