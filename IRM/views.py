from django.shortcuts import render
from models import IRM_Agency
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import PermissionDenied

from forms import Add_agency_Form
from models import IRM_Agency


# Create your views here.

def Landing(request):
    pass

notify = {}

def add_agency(request):
    notify = {}
    if request.method == 'POST':
        forms = Add_agency_Form(request.POST)
        if forms.is_valid():
            forms.Modified_by = str(request.user)
            forms.save()
            notify['level']   = 'success'
            notify['Message'] ='Agency Created Successfully'            
            forms = Add_agency_Form(user=request.user)
        else:
            notify['level']   = 'warning'
            notify['Message'] = 'Error Please Correct the below Errors'
            
    else:
        forms = Add_agency_Form()
    
    return render(request, 'IRM/add_agency.html', {'forms': forms, 'Form_method' : 'add_agency/' ,'Notify' : notify})


def list_agencies(request): 
    agencies_list_qs = IRM_Agency.objects.all()
    return render(request,'IRM/agency_list.html',{'Agencies_list':agencies_list_qs})

def edit_agency(request,Record_id):
    
    if request.method == 'POST':
        instance = IRM_Agency.objects.get(id=Record_id)
        forms = Add_agency_Form(request.POST or None, instance=instance)
        if forms.is_valid():
            forms.Modified_by = str(request.user)
            forms.save()
            notify['level']   = 'success'
            notify['Message'] ='Agency Details Updated Successfully'
            return HttpResponseRedirect('/IRM/list_agencies')        
            
        
    
    else:
        agency_detail= IRM_Agency.objects.get(pk=Record_id)
        forms = Add_agency_Form(instance=agency_detail)
        Form_Method = 'edit_agency/'+ Record_id
        
    return render(request, 'IRM/add_agency.html', {'forms': forms , 'Form_method' : Form_Method ,'Notify' : notify})

@csrf_protect
def delete_agency(request,Record_id):
    print Record_id
    Trans_Record = IRM_Agency.objects.get(id=Record_id)
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
        
