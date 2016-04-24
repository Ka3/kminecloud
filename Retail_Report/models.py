from __future__ import unicode_literals

from django.db import models




class Transaction_Table(models.Model):
    def __str__(self):
        return (self.Collection_Date).strftime("%Y-%m-%d %H:%M:%S")
    TIL1_Total  = models.DecimalField(max_digits=20, decimal_places=2)
    TIL2_Total  = models.DecimalField(max_digits=20, decimal_places=2)
    TIL1_Card   = models.DecimalField(max_digits=20, decimal_places=2)
    TIL1_Cash  = models.DecimalField(max_digits=20, decimal_places=2)
    Grand_Total = models.DecimalField(max_digits=20, decimal_places=2)
    Collection_Date = models.DateTimeField()
    Updated_Dated = models.DateTimeField(auto_now_add=True)
    Updated_User = models.CharField(max_length=200)
    Active_Flag = models.BooleanField(default=True)
    Bank_Deposit = models.DecimalField(max_digits=20, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.Grand_Total = self.TIL1_Total + self.TIL2_Total
        super(Transaction_Table, self).save(*args, **kwargs)


