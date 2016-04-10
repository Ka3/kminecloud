from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from form_wizard.forms import ContactForm1, ContactForm2, ContactForm3, ContactForm4
from views import ContactWizard
from form_wizard import views



urlpatterns = [
            url(r'^$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3, ContactForm4]) ),
            url(r'^(?i)profile/(?P<Record_id>[\w\d\ \-]+)$', views.Profile,name='profile view'),         
        ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
