from django import forms            
from django.contrib.auth.models import User
from Retail_Report.models import Transaction_Table  
from django.forms import ModelForm

from django.db.models import Q


class Transaction_Form(ModelForm):
	
	Grand_Total = forms.DecimalField(required=False)
	class Meta:
		model = Transaction_Table
		fields = '__all__'


