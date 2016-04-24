from django.conf.urls import url
from domain.views import SiteList,CreateSite,WebsiteDetailView
from domain import views
app_name = 'domain'
urlpatterns = [
    url(r'^$', SiteList.as_view(),name='site_list'),
    url(r'^create$', CreateSite.as_view(),name='create_site'),
    url(r'^get_expiry_date$', views.get_expiry_date ,name='get_expiry_date'),
    url(r'^(?i)delete_domain/(?P<Record_id>[\w\d\ \-]+)$', views.delete_domain,name='delete_domain'),
    url(r'^detail/(?P<pk>[-\w]+)/$', WebsiteDetailView.as_view(), name='domain-detail'),
]