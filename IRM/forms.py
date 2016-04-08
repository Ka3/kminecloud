from django.forms import ModelForm
from django import forms
from django.utils import timezone



from models import IRM_Agency



class Add_agency_Form(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Add_agency_Form, self).__init__(*args, **kwargs)       
        self.request = kwargs.pop('request', None)
        
        
    class Meta:
        model = IRM_Agency
        exclude = ['Created_By','Modified_by','created','modified']
        widgets = {
            'Location': forms.Select(attrs={'required': True}),
            'Agency_Type' : forms.Select(attrs={'required': True}),
            'Agency_Name' : forms.TextInput(attrs={'required': True}),
        }
    

    def save(self, *args, **kwargs):
       obj = super(Add_agency_Form, self).save(*args, **kwargs)
       obj.Modified_by = self.user
       obj.save()
       return obj   

 