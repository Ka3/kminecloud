from django.conf.urls import patterns, include, url
from Retail_Report import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
			url(r'^$', login_required(views.Daily_Update,login_url='/kmine_auth/login/'), name='index'),
			url(r'^(?i)update/', login_required(views.Daily_Update,login_url='/kmine_auth/login/'), name='Transaction'),
			url(r'^(?i)Monthly_Update/', login_required(views.Monthly_Update,login_url='/kmine_auth/login/'), name='Monthly_Update'),
			#url(r'^(?i)Monthly_Report/', login_required(views.Monthly_Report,login_url='/kmine_auth/login/'), name='Monthly_Report'),
			url(r'^(?i)Print_Report/(?P<month>[\w\d\ \-]+)/(?P<year>[\w\d\ \-]+)$', login_required(views.Print_Report,login_url='/kmine_auth/login/'), name='Print_Report'),
			url(r'^(?i)Sales_Report_custom/', login_required(views.Sales_Report_custom,login_url='/kmine_auth/login/'), name='Sales_Report_custom'),
			url(r'^(?i)Custom_sales_report/', login_required(views.Custom_sales_report,login_url='/kmine_auth/login/'), name='Custom_sales_report'),
			url(r'^(?i)Monthly_Report/', views.Monthly_Report, name='Monthly_Report'),
			url(r'^(?i)get_record/(?P<Record_id>[\w\d\ \-]+)$', views.get_record, name='get_record'),
			url(r'^(?i)change/(?P<Record_id>[\w\d\ \-]+)$', views.Delete_Record, name='Delete_Record'),
			url(r'^(?i)Print_Report_Audit/(?P<month>[\w\d\ \-]+)/(?P<year>[\w\d\ \-]+)$', login_required(views.Print_Report_Auditor,login_url='/kmine_auth/login/'), name='Print_Report_Auditor'),
			url(r'^(?i)Sales_Report_custom_Audit/', login_required(views.Sales_Report_custom_Auditor,login_url='/kmine_auth/login/'), name='Sales_Report_custom_Auditor'),
			url(r'^(?i)Custom_sales_report_Audit/', login_required(views.Custom_sales_report_Auditor,login_url='/kmine_auth/login/'), name='Custom_sales_report_Auditor'),
			
		)
