from django.db import models

# Create your models here.


class Partner(models.Model):
    name = models.CharField(max_length=256)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=11)
    born = models.DateField()
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Farm(models.Model):
    name = models.CharField(max_length=512)
    insc_state = models.CharField(max_length=56)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_partnership(self):
        return self.partners.all()


class Partnership(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT)
    percent = models.DecimalField(max_digits=4, decimal_places=2)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='partners')
    user = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.partner.name + ' ( ' + str(self.percent) + ' )'


class BankAccount(models.Model):
    name = models.CharField(max_length=512)
    account_number = models.CharField(max_length=56)
    agency = models.CharField(max_length=12)
    number = models.CharField(max_length=32)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        return self.name + ' (' + self.account_number + ')'


class Account(models.Model):
    name = models.CharField(max_length=512)
    number = models.CharField(max_length=32)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):

        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=512)
    cnpj = models.CharField(max_length=25)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    def __str__(self):
        return self.name + '( CNPJ '+ self.cnpj + ' )'


class Bill(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    TYPE_CHOICES = (
        ('Pagar', 'Pagar'),
        ('Receber', 'Receber')
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=12)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.PROTECT, related_name='bank_account')
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='bill_account')
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)
    description = models.CharField(max_length=512)
    date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    DOCUMENT_CHOICES = (
        ('NFE', 'NFE'),
        ('CONTRATO', 'CONTRATO'),
        ('RECIBO', 'RECIBO'),

    )
    document_type = models.CharField(choices=DOCUMENT_CHOICES, null=True, blank=True, max_length=20)
    document_number = models.IntegerField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=512)
    unity = models.CharField(max_length=512)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)