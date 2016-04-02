
from django.forms import ModelForm
from models import Person
from django import forms
from django.contrib.admin.templatetags.admin_static import static

class AdminDateWidget(forms.DateInput):
    @property
    def media(self):
        csss = {
            'all': ('admin/css/widgets.css',)
        }
        js = ["core.js","vendor/jquery/jquery.js","jquery.init.js","calendar.js", "admin/DateTimeShortcuts.js"]
        return forms.Media(js=[static('/admin/jsi18n/')] + [static("admin/js/%s" % path) for path in js],css=csss)

    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'vDateField', 'size': '10'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(AdminDateWidget, self).__init__(attrs=final_attrs, format=format)


class ContactForm1(ModelForm):
    
     class Meta:
        model = Person
        fields = ('first_name', 'last_name')
    
class ContactForm2(ModelForm):
    Date_of_Birth = forms.DateField(widget=AdminDateWidget)
    class Meta:
        model = Person
        fields = ('Date_of_Birth', 'Age', 'Gender')

class ContactForm3(ModelForm):
    class Meta:
        model = Person
        fields = ('Address_Line1', 'Address_Line2','Post_Code','City')
    
