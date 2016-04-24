from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.core.urlresolvers import reverse
from auditable.models import Auditable
from simple_history.models import HistoricalRecords

# Create your models here.
class Website(Auditable):
    def __str__(self):
        return self.domain_name
    
    domain_name = models.CharField(max_length=100,unique=True)
    domain_provider = models.CharField(max_length=100)
    expiry_date = models.DateField(blank=True,null=True)
    Hosting_server = models.CharField(max_length=100,blank=True,null=True)
    hosting_provider = models.CharField(max_length=100,blank=True,null=True)
    auto_renewal = models.BooleanField(default=False)
    comments = models.TextField(blank=True,null=True)
    history = HistoricalRecords()
    
    class Meta:
        ordering = ["-domain_name"]
    
    def get_absolute_url(self):
        return reverse("site_list")


class DNS_Info(Auditable):
    def __str__(self):
        return self.domain_name.domain_name
    domain_name = models.ForeignKey(Website,on_delete=models.CASCADE,related_name='%(class)s_DNS_Info')
    A_Record = models.CharField(max_length=100,blank=True,null=True)
    CName_Record = models.CharField(max_length=100,blank=True,null=True)
    MX_Record = models.CharField(max_length=100,blank=True,null=True)
    history = HistoricalRecords()
'''    
class SSL_Information:
    def __str__(self):
        return self.domain_name.domain_name
    domain_name = models.ForeignKey(Website,on_delete=models.CASCADE,related_name='%(class)s_SSL_Info')
    SSL_Presence = models.BooleanField(default=False)
    SSL_Expiry = models.DateField(blank=True,null=True)
    SSL_Provider = models.CharField(max_length=100,blank=True,null=True)
    history = HistoricalRecords()
'''                                    
    