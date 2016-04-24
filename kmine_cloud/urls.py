"""kmine_cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns,include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = [
    #url(r'',include('landing.urls'), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^(?i)Retail_Report/', include('Retail_Report.urls')),
    url(r'^(?i)kmine_auth/', include('kmine_auth.urls')),
    url(r'^kmine_auth/', include('django.contrib.auth.urls')),
    url(r'^home/', include('landing.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^form_wizard/', include('form_wizard.urls')),  
    url(r'^(?i)IRM/', include('IRM.urls')), 
    url(r'^(?i)domain/', include('domain.urls')),  
    
    #url(r'^(?i)events/', include('events.urls')),
   ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

