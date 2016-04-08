
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from IRM import views

urlpatterns = patterns('',
            url(r'^$', views.Landing, name='landing Page'),
            url(r'^(?i)add_agency/$', views.add_agency,name='Agency Add'),   
            url(r'^(?i)edit_agency/(?P<Record_id>[\w\d\ \-]+)$', views.edit_agency,name='Change Agency'), 
            url(r'^(?i)list_agencies/$', views.list_agencies,name='List of agencies'), 
            url(r'^(?i)delete_agency/(?P<Record_id>[\w\d\ \-]+)$', views.delete_agency,name='delete Agency'),
                 
        ) 
