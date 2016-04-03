
from django.forms import ModelForm
from models import Person
from django import forms
from django.contrib.admin.templatetags.admin_static import static


class AdminDateWidget(forms.DateInput):
    @property
    def media(self):
        '''
        csss = {
            'all': ('admin/css/widgets.css',)
        }
        '''
        js = ["core.js","vendor/jquery/jquery.js","jquery.init.js","calendar.js"]
        #return forms.Media(js=[static('/admin/jsi18n/')] + [static("admin/js/%s" % path) for path in js],css=csss)
        return forms.Media(js=[static('/admin/jsi18n/')] + [static("admin/js/%s" % path) for path in js])

    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'vDateField', 'size': '10'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(AdminDateWidget, self).__init__(attrs=final_attrs, format=format)


class ContactForm1(ModelForm):
     first_name = forms.CharField(widget=forms.TextInput(attrs={'required': 'true'}))
     E_Mail = forms.EmailField(widget=forms.EmailInput(attrs={'required': 'true'}))
     last_name = forms.CharField(widget=forms.TextInput(attrs={'required': 'true'}))
     
     Photo = forms.ImageField(widget=forms.FileInput(attrs={'onchange': 'readURL(this);'}),required=False)
     class Meta:
        model = Person
        fields = ('first_name',  'E_Mail', 'last_name', 'Photo')
    
class ContactForm2(ModelForm):
    Date_of_Birth = forms.DateField(widget=AdminDateWidget)
    Age = forms.IntegerField(widget=forms.NumberInput(attrs={'required': 'true'}))
    
    class Meta:
        model = Person
        fields = ('Date_of_Birth', 'Age', 'Gender')

class ContactForm3(ModelForm):
    class Meta:
        model = Person
        fields = ('Address_Line1', 'Address_Line2','Post_Code','City')
        

class ContactForm4(ModelForm):
     class Meta:  
          model = Person
          fields = ()
