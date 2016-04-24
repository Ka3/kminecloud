from django import forms
from domain.models import Website

class Future_DateWidget(forms.DateInput):
    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'fut_DateField', 'size': '10'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(Future_DateWidget, self).__init__(attrs=final_attrs, format=format)





class SiteForm(forms.ModelForm):
    class Meta:
        model=Website
        exclude = ['created_by','modified_by']
        widgets = {
            'domain_name': forms.TextInput(attrs={'required': True}),
            'domain_provider' : forms.TextInput(attrs={'required': True}),
            'expiry_date' : Future_DateWidget()
        }
    MX_Records = forms.CharField(required=False,widget=forms.TextInput())
    A_Record = forms.CharField(required=False,widget=forms.TextInput())
    field_order = ['domain_name',
                                'expiry_date',
                                'auto_renewal',
                                'A_Record',
                                'MX_Records',
                                'Hosting_server',
                                'hosting_provider',
                                'domain_provider',
                                'comments',
                               ]  
    
      