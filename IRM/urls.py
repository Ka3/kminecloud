
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from IRM import views

urlpatterns = [
            url(r'^$', views.Landing, name='landing Page'),
            url(r'^(?i)add_agency/$', views.add_agency, name='Agency Add'),   
            url(r'^(?i)edit_agency/(?P<Record_id>[\w\d\ \-]+)$', views.edit_agency,name='Change Agency'), 
            url(r'^(?i)list_agencies/$', views.list_agencies,name='List of agencies'), 
            url(r'^(?i)delete_agency/(?P<Record_id>[\w\d\ \-]+)$', views.delete_agency,name='delete Agency'),
            url(r'^(?i)add_panel_member/$', views.add_panel_member ,name='add_panel_member'),
            url(r'^(?i)list_panel_members/$', views.list_panel_members ,name='list_panel_members'),
            url(r'^(?i)test_child/$', views.test_child ,name='test_child'),
            url(r'^(?i)list_agency_admins/$', views.list_agency_admins ,name='list_agency_admins'),
            url(r'^(?i)add_agency_admin/$', views.add_agency_admin ,name='add_agency_admin'),
            url(r'^(?i)edit_agency_contact/(?P<Record_id>[\w\d\ \-]+)$', views.edit_agency_contact ,name='edit_agency_contact'),
            url(r'^(?i)delete_agency_contact/(?P<Record_id>[\w\d\ \-]+)$', views.delete_agency_contact ,name='delete_agency_contact'),
            
            
            
        ] 
