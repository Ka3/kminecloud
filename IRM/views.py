from django.shortcuts import render

from django.http import HttpResponseRedirect,HttpResponseForbidden,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import PermissionDenied

from models import IRM_Agency,IRM_Agency_Admin_Contact
from forms import Add_agency_Form,Add_Agency_Admin_Form

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Landing(request):
    pass

notify = {}

@login_required
def add_agency(request):
    notify = {}
    Form_Title = 'Add Agency'
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
    
    return render(request, 'IRM/add_agency.html', {'Form_Title':Form_Title, 'forms': forms, 'Form_method' : 'add_agency/' ,'Notify' : notify})

@login_required
def list_agencies(request):
    agencies_list_qs = IRM_Agency.objects.all()
    return render(request,'IRM/agency_list.html',{'Agencies_list':agencies_list_qs})
@login_required
def edit_agency(request,Record_id):
    Form_Title = 'Update Agency Information'
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
        
    return render(request, 'IRM/add_agency.html', {'Form_Title':Form_Title,'forms': forms , 'Form_method' : Form_Method ,'Notify' : notify})

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

@login_required
def list_agency_admins(request):
    agencies_contact_list_qs = IRM_Agency_Admin_Contact.objects.all()
    return render(request,'IRM/agency_CONTACT_list.html',{'Contact_list':agencies_contact_list_qs})
    return HttpResponse('<h1>List Panel Admins<h1>')

@login_required
def add_agency_admin(request):
    notify = {}
    Form_Title = 'Add Agency Admin Contact'
    if request.method == 'POST':
        forms = Add_Agency_Admin_Form(request.POST)
        if forms.is_valid():
            forms.Modified_by = str(request.user)
            forms.save()
            notify['level']   = 'success'
            notify['Message'] ='Agency Admin Contact added Successfully'            
            forms = Add_Agency_Admin_Form(user=request.user)
        else:
            notify['level']   = 'warning'
            notify['Message'] = 'Error Please Correct the below Errors'
            
    else:
        forms = Add_Agency_Admin_Form()
    
    return render(request, 'IRM/add_agency.html', {'Form_Title':Form_Title, 'forms': forms, 'Form_method' : 'add_agency_admin/' ,'Notify' : notify})
    #return HttpResponse('<h1>Add Agency Admins<h1>')
@login_required
def edit_agency_contact(request,Record_id):
    Form_Title = 'Update Agency Contact Information'
    if request.method == 'POST':
        instance = IRM_Agency_Admin_Contact.objects.get(id=Record_id)
        forms = Add_Agency_Admin_Form(request.POST or None, instance=instance)
        if forms.is_valid():
            forms.Modified_by = str(request.user)
            forms.save()
            notify['level']   = 'success'
            notify['Message'] ='Contact Details Updated Successfully'
            return HttpResponseRedirect('/IRM/list_agency_admins')        
            
        
    
    else:
        agency_detail= IRM_Agency_Admin_Contact.objects.get(pk=Record_id)
        forms = Add_Agency_Admin_Form(instance=agency_detail)
        Form_Method = 'edit_agency_contact/'+ Record_id
        
    return render(request, 'IRM/add_agency.html', {'Form_Title':Form_Title,'forms': forms , 'Form_method' : Form_Method ,'Notify' : notify})

def delete_agency_contact(request,Record_id):
    print Record_id
    Trans_Record = IRM_Agency_Admin_Contact.objects.get(id=Record_id)
    if request.method == 'POST': 
        try:
            Trans_Record.delete()
            print "Delete Successful"
            notify['level']   = 'success'
            notify['Message'] ='Contact  deleted  Successfully'
        except:
            print "Delete record Failed"
            notify['level']   = 'warning'
            notify['Message'] = 'Contact Deletion Failed'
        #return HttpResponseRedirect('/IRM/list_agency_admins') 
        return render(request, 'IRM/notify.html', {'Notify' : notify})
    else:
        raise PermissionDenied




@login_required
def add_panel_member(request):
    return HttpResponse('<h1>Add Panel Member<h1>')

@login_required
def list_panel_members(request):
    return HttpResponse('<h1>List Panel Member<h1>')

@login_required
def edit_panel_member(request,Record_id):
    return HttpResponse('<h1>Edit Panel Member<h1>')

@login_required
def delete_panel_member(request,Record_id):
    return HttpResponse('<h1>Delete Panel Member<h1>')

@login_required
def test_child(request):
    pass
        
        
