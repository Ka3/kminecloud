from django.conf.urls import patterns, include, url
from events import views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
            url(r'^$', views.index, name='events landing'),
            url(r'^(?i)get_events$', views.get_events, name='get_events'),
            
        )


'http://dev.kmine.com:8001/mysite?start=2016-03-27&end=2016-05-08&_=1458774645111'