from django.forms import ModelForm
from django import forms
from django.utils import timezone



from models import IRM_Agency,IRM_Agency_Admin_Contact



class Add_agency_Form(ModelForm):
   
    #Modified_by = Modified_by.CharField(widget = forms.HiddenInput(), required = False)
        
    class Meta:
        model = IRM_Agency
        exclude = ['Created_by','created','modified','Modified_by']
        widgets = {
            'Location': forms.Select(attrs={'required': True}),
            'Agency_Type' : forms.Select(attrs={'required': True}),
            'Agency_Name' : forms.TextInput(attrs={'required': True}),
        }

class Add_Agency_Admin_Form(ModelForm): 
    
    class Meta:
        model = IRM_Agency_Admin_Contact
        exclude = ['Created_by','Modified_by','created','modified','Address_Line_4']
        widgets = {
            'Title': forms.Select(attrs={'required': True}),
            'Firstname' : forms.TextInput(attrs={'required': True}),
            'Surname' : forms.TextInput(attrs={'required': True}),
            'Position' : forms.TextInput(attrs={'required': True}),
            'Address_Line_1' : forms.TextInput(attrs={'required': True}),
            'Postcode' : forms.TextInput(attrs={'required': True}),
            'Role' : forms.Select(attrs={'required': True}),
            'Notes' : forms.Textarea(attrs={'cols': 30, 'rows': 4}),
            
        }