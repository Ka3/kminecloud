from django.conf.urls import patterns, include, url
from landing import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'console/^$', login_required(views.console,login_url='/kmine_auth/login/'), name='home'),
)	
