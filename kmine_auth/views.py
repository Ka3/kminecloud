from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.views import password_reset

# Create your views here.

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('kmine_auth/login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    next_URL_raw = request.META.get('HTTP_REFERER')
    try:
        next_URL = next_URL_raw.split('=')[1]
    except:
        next_URL = "/home"
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user) 
        print 'authenticated'
        try:        
            next_URL =user.user_profile.user_URLField
        except:
            next_URL = next_URL
        print next_URL
        return HttpResponseRedirect(next_URL)
    else:
        Error_Text = "Login Details are invalid"
        return render(request, 'kmine_auth/login.html',{'Error_Text': Error_Text})


	
def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/kmine_auth/login/',)

def reset_password(request):
    pass
'''
def forgot_password(request):
    if request.method == 'POST':
        return password_reset(request, 
            from_email=request.POST.get('email'))
    else:
        return render(request, 'kmine_auth/forgot_password.html')
'''


def forgot_password(request, template_name='kmine_auth'):
    return password_reset(request, template_name)