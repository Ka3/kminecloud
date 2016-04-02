from django.conf.urls import patterns, include, url
from events import views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
            url(r'^$', views.index, name='events landing'),
            url(r'^(?i)get_events$', views.get_events, name='get_events'),
            url(r'^(?i)remove_event$', views.remove_event, name='remove_event'),
            url(r'^(?i)create_event/', views.create_event, name='create_event'),
        )


