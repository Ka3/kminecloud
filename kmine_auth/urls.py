from django.conf.urls import patterns, include, url
from kmine_auth import views
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.conf.urls import *


urlpatterns = patterns('',
			url(r'^login/', views.login,name='login'),
			url(r'^logout/$', views.log_out, name='logout'),
			url(r'^auth/', views.auth_view,name='auth_view'),
			url(r'^forgot-password/$',  views.forgot_password,    name="forgot-password" ),


			)

