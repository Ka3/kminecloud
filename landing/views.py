from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

# Create your views here.

def index(request):
    template = loader.get_template('base/__base.html')
    context = RequestContext(request)
    """    
    U = User.objects.get(username=request.user)
    Company_list = request.session['company_list']
    FirstName =  U.first_name
    context['user']= FirstName
    context['Company_list'] = Company_list
    context['org_name'] = request.session['org_name']
    print context['org_name']
    """
    return HttpResponse(template.render(context))

def console(request):
	template = loader.get_template('base/__base.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))
