from django.contrib import admin

# Register your models here.

from .models import Transaction_Table


class Shop_Admin(admin.ModelAdmin):
    list_display = ('Collection_Date', 'TIL1_Card','TIL1_Cash','TIL1_Total','Grand_Total','Bank_Deposit','Updated_Dated','Updated_User','Active_Flag')
    

admin.site.register(Transaction_Table,Shop_Admin)