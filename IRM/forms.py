from django.forms import ModelForm
from django import forms
from django.utils import timezone
from django.contrib.admin.templatetags.admin_static import static



from models import IRM_Agency,IRM_Agency_Admin_Contact,IRM_PanelContact,IRM_Case,IRM_Case_dup


class Future_DateWidget(forms.DateInput):
    def __init__(self, attrs=None, format=None):
        final_attrs = {'class': 'fut_DateField', 'size': '10'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(Future_DateWidget, self).__init__(attrs=final_attrs, format=format)
       
        
class DOB_DateWidget(forms.DateInput):
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
        super(DOB_DateWidget, self).__init__(attrs=final_attrs, format=format)



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
        
class Panel_Form1(ModelForm):
     class Meta:
        model = IRM_PanelContact
        fields = ('Principal_IRMLocationID_FK', 'Two_IRMLocationID_FK', 'Three_IRMLocationID_FK', 'Four_IRMLocationID_FK', 'Title','Ethnicity', 'Firstname','Surname','Panel_Role','Participant_Type','Position','Gender')
        widgets = {
            'Principal_IRMLocationID_FK': forms.Select(attrs={'required': True}),
            'Two_IRMLocationID_FK' : forms.Select(attrs={'required': True}),
            'Title' : forms.Select(attrs={'required': True}),
            'Firstname' : forms.TextInput(attrs={'required': True}),
            'Surname' : forms.TextInput(attrs={'required': True}),
            'Ethnicity' : forms.Select(attrs={'required': True}),
            'Panel_Role' : forms.Select(attrs={'required': True}),
            'Participant_Type' : forms.TextInput(attrs={'required': True}),
            'Gender' : forms.Select(attrs={'required': True}),
        }
        
 
class Panel_Form2(ModelForm):
    class Meta:
        model = IRM_PanelContact
        fields = ('Home_Address_Line_1', 'Home_Address_Line_2', 'Home_Address_Line_3','Home_Address_Line_4','Home_Town','Home_County','Home_Postcode','Home_Phone')
        widgets = {
            'Home_Address_Line_1': forms.TextInput(attrs={'required': True}),
            'Home_Town' : forms.TextInput(attrs={'required': True}),
            'Home_Postcode' : forms.TextInput(attrs={'required': True}),
            'Work_Address_Line_1' : forms.TextInput(attrs={'required': True}),
            'Work_Town' : forms.TextInput(attrs={'required': True}),
            'Work_Postcode' : forms.TextInput(attrs={'required': True}),
            'Appointment_Date' : forms.Select(attrs={'required': True}),
        }

class Panel_Form3(ModelForm):
     Appointment_Date = forms.DateField(widget=Future_DateWidget(attrs={'required': 'true'}))
     class Meta:  
          model = IRM_PanelContact
          fields = ('Work_Address_Line_1','Work_Address_Line_2','Work_Address_Line_3','Work_Address_Line_4','Work_Town','Work_County','Work_Postcode','Work_Phone','Mobile','Email','Fax','Appointment_Date')
          widgets = {
            'Work_Address_Line_1': forms.TextInput(attrs={'required': True}),
            'Work_Postcode' : forms.TextInput(attrs={'required': True}),
            'Work_Town' : forms.TextInput(attrs={'required': True}),
        }
class Panel_Form4(ModelForm):
     class Meta:  
          model = IRM_PanelContact
          fields = ()
               
class Case_Form1(ModelForm):
    class Meta:
        model = IRM_Case
        fields = ('Type','IRM_Reference', 'IRM_Location', 'Agency', 'Agency_Decision','Legal_Advisor', 'Date_Appliction_Received','Report_Status', 'Inter_Country', 'Major_Recommendation','Case_Notes' )
        widgets = {
            'Inter_Country': forms.NullBooleanSelect(attrs={'required': True}),
            'Type' : forms.Select(attrs={'required': True}),
            'Agency' : forms.Select(attrs={'required': True}),
            'Date_Appliction_Received' : forms.TextInput(attrs={'required': True}),
            'Major_Recommendation' : forms.TextInput(attrs={'required': True}),
            'IRM_Location' : forms.Select(attrs={'required': True}),
            'Legal_Advisor' : forms.TextInput(attrs={'required': True}),
        }

class Case_Form2(ModelForm):
    class Meta:
        model = IRM_Case
        fields = ('Person_1_Title','Person_1_Gender','Person_1_FirstName','Person_1_Surname','Person_1_Ethnicity','Person_1_DateOfBirth','Marital_Status','Salutation')

class Case_Form3(ModelForm):
    class Meta:
        model = IRM_Case
        fields = ('Person_2_Title','Person_2_Gender','Person_2_FirstName','Person_2_Surname','Person_2_Ethnicity','Person_2_DateOfBirth')

class Case_Form4(ModelForm):
    class Meta:
        model = IRM_Case
        fields = ('Address_Line_1','Address_Line_2','Address_Line_3','Address_Line_4','Town','County','Postcode','Phone','Mobile','Email','Fax','ContactNotes')
class Case_Form5(ModelForm):
    class Meta:
        model = IRM_Case
        fields = ()