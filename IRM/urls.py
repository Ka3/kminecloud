
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from IRM import views
from IRM.forms import Panel_Form1, Panel_Form2, Panel_Form3, Panel_Form4
from views import ContactWizard

urlpatterns = [
               
            url(r'^$', views.Landing, name='landing Page'),
            url(r'^(?i)add_agency/$', views.add_agency, name='Agency Add'),   
            url(r'^(?i)edit_agency/(?P<Record_id>[\w\d\ \-]+)$', views.edit_agency,name='Change Agency'), 
            url(r'^(?i)list_agencies/$', views.list_agencies,name='List of agencies'), 
            url(r'^(?i)delete_agency/(?P<Record_id>[\w\d\ \-]+)$', views.delete_agency,name='delete Agency'),
           
            ###
            url(r'^(?i)list_agency_admins/$', views.list_agency_admins ,name='list_agency_admins'),
            url(r'^(?i)add_agency_admin/$', views.add_agency_admin ,name='add_agency_admin'),
            url(r'^(?i)edit_agency_contact/(?P<Record_id>[\w\d\ \-]+)$', views.edit_agency_contact ,name='edit_agency_contact'),
            url(r'^(?i)delete_agency_contact/(?P<Record_id>[\w\d\ \-]+)$', views.delete_agency_contact ,name='delete_agency_contact'),
            
            ####  
                      
            url(r'^(?i)add_panel_member/', ContactWizard.as_view([Panel_Form1, Panel_Form2, Panel_Form3, Panel_Form4]) , name='add_panel_member' ),
            url(r'^(?i)list_panel_members/$', views.list_panel_members ,name='list_panel_members'),
            url(r'^(?i)list_legal_advisors/$', views.list_legal_advisors ,name='list_legal_advisors'),
            url(r'^(?i)deactivate_panel_member/(?P<Record_id>[\w\d\ \-]+)$', views.deactivate_panel_member ,name='deactivate_panel_member'),
            
        ] 
