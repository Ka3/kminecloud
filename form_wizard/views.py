from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
import logging
from django.forms.models import construct_instance
from .models import Person
from forms import ContactForm1,ContactForm2,ContactForm3
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings


# Create your views here.
def index(request):
    pass


class ContactWizard(SessionWizardView):
    
    def get_template_names(self):
        print self.steps.current
        print type(self.steps.current)
        if str(self.steps.current) == '3':
            print 'step 4'
            return 'form_wizard/form_summary.html'
        else:
            print self.steps.current
            return 'form_wizard/form_wizard.html'
    
    
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))
    template_name=""
    
    
    def get_context_data(self, form, **kwargs):
        context = super(ContactWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == '3':
            print 'This is Step4'
            Field_order = [ 
                           ['first_name',  'E_Mail', 'last_name', 'Photo'],
                           ['Date_of_Birth', 'Age', 'Gender'],
                           ['Address_Line1', 'Address_Line2','Post_Code','City'],
                           ]
            context.update({'all_data': self.get_all_cleaned_data(),
                            'Field_order' : Field_order                            
                            })
        return context
            
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        return HttpResponseRedirect('/form_wizard/profile/'+ str(form_data))
        
    

def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    new = Person()
    for form in form_list:
        new = construct_instance(form, new, form._meta.fields, form._meta.exclude)
    new.save()
    return new.id
    #return form_data


def Profile(request,Record_id):
    Trans_Record = Person.objects.filter(pk=Record_id)[0]
    print Trans_Record
    Field_order = [ 
                           ['first_name',  'E_Mail', 'last_name', 'Photo'],
                           ['Date_of_Birth', 'Age', 'Gender'],
                           ['Address_Line1', 'Address_Line2','Post_Code','City'],
                           ]
    return render_to_response('form_wizard/profile.html', {'profile' : Trans_Record ,'Field_order' : Field_order })
    
    
    
    