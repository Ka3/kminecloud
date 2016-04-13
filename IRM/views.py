from django.shortcuts import render

from django.http import HttpResponseRedirect,HttpResponseForbidden,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import PermissionDenied

from models import IRM_Agency,IRM_Agency_Admin_Contact,IRM_PanelContact
from forms import Add_agency_Form,Add_Agency_Admin_Form,Panel_Form1,Panel_Form2,Panel_Form3,Panel_Form4

from django.contrib.auth.decorators import login_required

from formtools.wizard.views import SessionWizardView

from django.forms.models import construct_instance

from django.db.models import Count
from django.db.models import Q

# Create your views here.
@login_required
def Landing(request):
    
    #import ipdb; ipdb.set_trace()
    Agency_admins = 10000
    Panel_admins = 10000
    Panel_members = 10000
    
    Total_Cases = 10000
    Open_Cases = 10000
    
    Pay_load = {'Agency_list' :IRM_Agency.objects.all().count(),
                'Agency_admins': IRM_Agency_Admin_Contact.objects.all().count(),
                'Panel_admins' : IRM_PanelContact.objects.all().count(),
                'Panel_members' : Panel_members,
                'Total_Cases' : Total_Cases,
                'Open_Cases' : Open_Cases,
                
                }
    
    return render(request, 'IRM/Landing.html', {'Pay_load':Pay_load})


notify = {}

@login_required
def add_agency(request):
    notify = {}
    Form_Title = 'Add Agency'
    if request.method == 'POST':
        forms = Add_agency_Form(request.POST)
        if forms.is_valid():
            form_tmp = forms.save(commit=False)
            print 'request.user : ',request.user
            form_tmp.Modified_by = str(request.user)
            #import ipdb; ipdb.set_trace()
            form_tmp.save()
            notify['level']   = 'success'
            notify['Message'] ='Agency Created Successfully'            
            forms = Add_agency_Form()
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
            form_tmp = forms.save(commit=False)
            print 'request.user : ',request.user
            form_tmp.Modified_by = str(request.user)
            form_tmp.save()
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
            form_tmp = forms.save(commit=False)
            print 'request.user : ',request.user
            form_tmp.Modified_by = str(request.user)
            form_tmp.save()
            forms = Add_Agency_Admin_Form()
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
            form_tmp = forms.save(commit=False)
            print 'request.user : ',request.user
            form_tmp.Modified_by = str(request.user)
            form_tmp.save()
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
def list_panel_members(request):
    panel_member_list_qs = IRM_PanelContact.objects.all()
    return render(request,'IRM/panel_CONTACT_list.html',{'Contact_list':panel_member_list_qs})


@login_required
def list_legal_advisors(request):
    panel_member_list_qs = IRM_PanelContact.objects.filter(Q(Status='Active'),Q(Panel_Role=10))
    return render(request,'IRM/panel_CONTACT_list.html',{'Contact_list':panel_member_list_qs})

@login_required
def edit_panel_member(request,Record_id):
    return HttpResponse('<h1>Edit Panel Member<h1>')

@login_required
def delete_panel_member(request,Record_id):
    return HttpResponse('<h1>Delete Panel Member<h1>')

def deactivate_panel_member(request,Record_id):
    print Record_id
    Trans_Record = IRM_PanelContact.objects.get(id=Record_id)
    if request.method == 'POST': 
        try:
            Trans_Record.Status = 'Inactive'
            Trans_Record.save()
            print "Delete Successful"
            notify['level']   = 'success'
            notify['Message'] ='Contact  Deactivated  Successfully'
        except:
            print "Deactivation Failed"
            notify['level']   = 'warning'
            notify['Message'] = 'Unable to change the contact status'
        #return HttpResponseRedirect('/IRM/list_agency_admins') 
        return render(request, 'IRM/notify.html', {'Notify' : notify})
    else:
        raise PermissionDenied

@login_required
def test_child(request):
    pass


TEMPLATES_Panel = {"0": "IRM/panel_wizard_step1.html",
                   "1": "IRM/panel_wizard_step2.html",
                   "2": "IRM/panel_wizard_step3.html",
                   "3": "IRM/panel_wizard_step4.html",
                  }

      
class ContactWizard(SessionWizardView):
    
    def get_template_names(self):
        print   'current_step :', self.steps.current 
        return [TEMPLATES_Panel[self.steps.current]] 
            
    
    def get_context_data(self, form, **kwargs):
        context = super(ContactWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == '3':
            print 'This is Step3'
            Field_order = [ 
                           ['Principal_IRMLocationID_FK',  'Two_IRMLocationID_FK', 'Three_IRMLocationID_FK', 'Four_IRMLocationID_FK'],
                           ['Title', 'Firstname', 'Surname','Gender','Ethnicity','Participant_Type','Panel_Role','Position'],
                           ['Home_Address_Line_1', 'Home_Address_Line_2','Home_Address_Line_3','Home_Address_Line_4','Home_Town','Home_County','Home_Postcode','Home_Phone'],
                           ['Work_Address_Line_1','Work_Address_Line_2','Work_Address_Line_3','Work_Address_Line_4','Work_Town','Work_County','Work_Postcode','Work_Phone'],
                           ['Mobile','Email','Fax','Appointment_Date'],
                           ['Notes']
                           ]
            #import ipdb; ipdb.set_trace()
            context.update({'all_data': self.get_all_cleaned_data(),
                            'Field_order' : Field_order                            
                            })
        return context
            
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        return HttpResponseRedirect('/form_wizard/profile/'+ str(form_data))
    
def process_form_data(form_list):
    print 'Calling Processing Form Data'
    form_data = [form.cleaned_data for form in form_list]
    new = IRM_PanelContact()
    for form in form_list:
        print 'corstructing form' 
        new = construct_instance(form, new, form._meta.fields, form._meta.exclude)
    sara = new.save()
    print 'saved to DB'
    return new.id

