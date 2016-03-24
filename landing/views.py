from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    template = loader.get_template('base/__base.html')
    context = RequestContext(request)
    try:   
        U = User.objects.get(username=request.user)
        Company_Name = U.user_profile.user_Default_org
        FirstName =  U.first_name
        context['user']= FirstName
        context['Company_Name'] = Company_Name
    
    except:
        pass

    return HttpResponse(template.render(context))

def console(request):
	template = loader.get_template('base/__base.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))
