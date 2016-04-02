from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required


from form_wizard.forms import ContactForm1, ContactForm2, ContactForm3
from views import ContactWizard



urlpatterns = patterns('',
            url(r'^$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
        )
