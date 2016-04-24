from django.contrib import admin

# Register your models here.
from domain.models import Website,DNS_Info

admin.site.register(Website)
admin.site.register(DNS_Info)
