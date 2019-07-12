from django.contrib import admin
from .models import *

class PartnershipInline(admin.TabularInline):
    model =  Partnership

class FarmAdmin(admin.ModelAdmin):
    model = Farm
    inlines = [
        PartnershipInline
    ]
# Register your models here.
admin.site.register(Partner)
admin.site.register(Farm, FarmAdmin)
admin.site.register(Partnership)
admin.site.register(Provider)
admin.site.register(Account)
admin.site.register(BankAccount)
admin.site.register(Bill)
admin.site.register(Product)