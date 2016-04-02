from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
 	Gender_Choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'TransGender'),
   			 )
	first_name = models.CharField("First Name",max_length=30)
	last_name = models.CharField(max_length=30)
	Date_of_Birth = models.DateField()
	Age = models.IntegerField()
	Gender = models.CharField(max_length=1, choices=Gender_Choices)
	Address_Line1 = models.CharField(max_length=100)
	Address_Line2 = models.CharField(max_length=100)
	Post_Code = models.CharField(max_length=100)
	City = models.CharField(max_length=100)
      
