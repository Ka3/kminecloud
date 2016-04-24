from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from domain.models import Website,DNS_Info
from django.views.generic.edit import FormView
from forms import SiteForm
from auditable.views import AuditableMixin
from django_ajax.decorators import ajax
import whois
from datetime import datetime
import socket
import dns.resolver

from django.views.generic.detail import DetailView

from django.views.decorators.csrf import csrf_protect
notify = {}
class SiteList(ListView):
    template_name = 'domain/generic_list.html'
    model = Website
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SiteList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['Title'] = 'Sites'
        context['query_list'] = Website.objects.all()
        context['Columns'] = [  'expiry_date',
                                'domain_provider',
                                'auto_renewal',
                               ]
        #import ipdb;ipdb.set_trace()
        return context
    
class CreateSite(FormView):
    template_name = 'domain/CreateSite.html'
    form_class = SiteForm
    success_url = '/domain'
    def form_valid(self, form, ):
        try:
            if not form.instance.created_by_id :
                form.instance.created_by  = self.request.user
                
        except:
            form.instance.created_by  = self.request.user
            
        form.instance.modified_by = self.request.user
        dom_key = form.save()
        sar = DNS_Info( domain_name = dom_key,
                        A_Record=self.request.POST['A_Record'],
                        MX_Record= self.request.POST['MX_Records']
                        
                      )
        try:
            if not sar.created_by_id :
                sar.created_by  = self.request.user
                
        except:
            sar.created_by  = self.request.user
        sar.modified_by = self.request.user
        sar.save()
        
        return super(CreateSite, self).form_valid(form)

@ajax
def get_expiry_date(request):
    site_name = request.POST['site_name']
    '''
    mx= ''
    for x in dns.resolver.query(site_name, 'MX'):
            mx = mx + (x.to_text()).replace('.','') + ', '
    print mx
    '''
    try:
        w = whois.whois(site_name)
        print w
        exp_date =  (w.expiration_date).strftime('%m/%d/%Y')
        registrar = w.registrar_url
        ip_addr = socket.gethostbyname(site_name)
        hosted_server =socket.gethostbyaddr(ip_addr)
        mx =''
        for x in dns.resolver.query(site_name, 'MX'):
            mx = mx + (x.to_text()).replace('.','') + ', '
        print mx
            
    except:
        exp_date =  'Domain Not Found'
        registrar = ''
        ip_addr = ''
        hosted_server = ''
        mx = ''
    
    json_data = {
        'exp_date': exp_date,
        'registrar' : registrar,
        'ip_addr' : ip_addr,
        'hosted_server' : hosted_server,
        'mx' : mx
    }
    print json_data
    return json_data

@csrf_protect
def delete_domain(request,Record_id):
    print Record_id
    Trans_Record = Website.objects.get(id=Record_id)
    if request.method == 'POST': 
        try:
            Trans_Record.delete()
            print "Delete Successful"
            notify['level']   = 'success'
            notify['Message'] ='Agency deleted  Successfully'
        except:
            print "Delete record Failed"
            notify['level']   = 'warning'
            notify['Message'] = 'Agency Deletion Failed'
        
        return render(request, 'IRM/notify.html', {'Notify' : notify})
    else:
        raise PermissionDenied

class WebsiteDetailView(DetailView):

    model = Website

    def get_context_data(self, **kwargs):
        #import ipdb; ipdb.set_trace()
        context = super(WebsiteDetailView, self).get_context_data(**kwargs)
        context['dns_info'] = DNS_Info.objects.filter(domain_name__domain_name=self.object.domain_name)[0]
        #context['now'] = timezone.now()
        return context
    
    
    
    
    