from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from formtools.wizard.views import SessionWizardView
import logging
from django.forms.models import construct_instance
from .models import Person
from forms import ContactForm1,ContactForm2,ContactForm3


# Create your views here.
def index(request):
    pass


class ContactWizard(SessionWizardView):
    template_name="form_wizard/form_wizard.html"
    def get_templates_name(self):
        return [TEST_TEMPLATES[self.steps.current]]
            
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        return render_to_response('form_wizard/done.html', {'form_data': form_data})

def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    new = Person()
    for form in form_list:
        new = construct_instance(form, new, form._meta.fields, form._meta.exclude)
    new.save()
    return redirect('/')

    