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

    def __str__(self):
        return self.name

    def get_partnership(self):
        return self.parterns.all()

class Partnership(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT)
    percent = models.DecimalField(max_digits=4, decimal_places=2)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='partners')

    def __str__(self):
        return self.partner.name + '('+ str(self.percent) +')'


class Account(models.Model):
    name = models.CharField(max_length=512)
    number = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField(max_length=512)
    cnpj = models.CharField(max_length=25)


    def __str__(self):
        return self.name

class Bill(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    TYPE_CHOICES = (
        ('Pagar', 'Pagar'),
        ('Receber', 'Receber')
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=12)
    bank_account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='bank_account')
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='bill_account')
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)
    description = models.CharField(max_length=512)



class Product(models.Model):
    pass
