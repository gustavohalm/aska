from rest_framework import serializers
from erp import models


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provider
        fields = '__all__'
        read_only_fields = ['id', 'user']


class BillSerializer(serializers.ModelSerializer):
    provider = ProviderSerializer(many=False)
    class Meta:
        model = models.Bill
        fields = '__all__'
        read_only_fields = ['id', 'user']


class FarmSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = models.Farm
        fields = '__all__'
        read_only_fields = [ 'id', 'user']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partner
        fields = '__all__'
        read_only_fields = ['id', 'user']


class PartnershipSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = models.Partnership
        fields = '__all__'
        read_only_fields = ['id', ]


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BankAccount
        fields = '__all__'
        read_only_fields = ['id', 'user',]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = models.Account
        fields = '__all__'
        read_only_fields = ['id', 'user']