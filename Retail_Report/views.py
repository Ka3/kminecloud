from django.shortcuts import render_to_response,render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.template.context_processors import csrf
from django.contrib import auth
from forms import Transaction_Form
from Retail_Report.models import Transaction_Table  
from datetime import date
from datetime import datetime
from django.forms.formsets import formset_factory
from functools import partial, wraps
from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg
#from models import san_mas_Invoice_details


from calendar import HTMLCalendar
from itertools import groupby
from django.utils.html import conditional_escape as esc
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
import json

# Create your views here.


def index(request):
    template = loader.get_template('__base.html')
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


def Daily_Update(request):
    today = date.today()
    my_workouts = Transaction_Table.objects.order_by('Collection_Date').filter(Q(
    Collection_Date__year=int(today.year), Collection_Date__month=int(today.month)),Q(Active_Flag=True),Q(Updated_User=request.user)
  )
    cal = WorkoutCalendar(my_workouts).formatmonth(int(today.year), int(today.month))
    user=request.user
    if request.method == 'POST':
        today = date.today()
        my_invoices_qs = Transaction_Table.objects.filter(Q(Collection_Date__year=today.year, Collection_Date__month=today.month),Q(Active_Flag=True),Q(Updated_User=request.user))
        form = Transaction_Form(request.POST)
        print form
        if form.is_valid():
            form.save()
            print "Form Saved"
            form = Transaction_Form(initial={'Updated_User': request.user,'Active_Flag':True})
            my_workouts = Transaction_Table.objects.order_by('Collection_Date').filter(Q(Collection_Date__year=int(today.year), Collection_Date__month=int(today.month)),Q(Active_Flag=True),Q(Updated_User=request.user) )
            cal = WorkoutCalendar(my_workouts).formatmonth(int(today.year), int(today.month))
            return render(request,'Retail_Report/Transaction_Form.html',{"Updated_User" :request.user ,'form': form, 'my_invoices_qs':my_invoices_qs,'calendar': mark_safe(cal),})  
   
        else:
            print 'Form is not valid'
        return render(request,'Retail_Report/Transaction_Form.html',{"Updated_User" :request.user ,'form': form, 'my_invoices_qs':my_invoices_qs,'calendar': mark_safe(cal),})  

    else:
        #form = Transaction_Form(initial={'user_id': request.user})
        
        form = Transaction_Form(initial={'Updated_User': request.user,'Active_Flag':True})
        today = date.today()
        my_invoices_qs = Transaction_Table.objects.order_by('Collection_Date').filter(Q(Collection_Date__year=today.year, Collection_Date__month=today.month), Q(Active_Flag=True),Q(Updated_User=request.user)) 
        print form
        return render(request, 'Retail_Report/Transaction_Form.html', {"Updated_User" :user , 'form': form , 'my_invoices_qs':my_invoices_qs, 'calendar': mark_safe(cal)} )

"""
def Monthly_Update(request):
    user=request.user
    return render(request, 'Retail_Report/calender.html', {"Updated_User" :user} )
"""

def Monthly_Update(request):
    user=request.user
    SalesFormSet_tmp = formset_factory(Transaction_Form )
    print SalesFormSet_tmp
    
    return render(request, 'Retail_Report/Monthly_Transaction_Form.html', {"Updated_User" :user , "SalesFormSet":SalesFormSet_tmp} )



def Accountant_Report(request):
    
    
    today = date.today()
    month = today.month
    my_invoices_qs = Transaction_Table.objects.order_by('Collection_Date').filter(Q(Collection_Date__year=today.year, Collection_Date__month=today.month),Q(Active_Flag=True),Q(Updated_User=request.user))
    
    (Q(user_id="athipathi"),Q(org_name="Kmine Info Solutions"))
    return render(request, 'Retail_Report/Accountant_print_invoice.html', { 'Month':today , 'my_invoices_qs':my_invoices_qs})

def Partner_Report(request):
    if request.method == 'POST':
        today = date.today()
        month = today.month
        my_invoices_qs = Transaction_Table.objects.order_by('Collection_Date').filter(Q(Collection_Date__year=today.year, Collection_Date__month=today.month),Q(Active_Flag=True),Q(Updated_User=request.user))
        return render(request, 'Retail_Report/Partner_print_invoice.html', { 'Month':today , 'my_invoices_qs':my_invoices_qs})
    else:
        pass
        
def Sales_Report_custom(request):

    return render(request, 'Retail_Report/Invoice_report_custom.html', {})

def Sales_Report_custom_Auditor(request):

    return render(request, 'Retail_Report/Invoice_report_custom_Auditor.html', {})

def Custom_sales_report(request):
    if request.POST:
        start_data = str((request.POST['startdate'])).lstrip().rstrip()
        print start_data
        start_date_object = datetime.strptime(start_data,'%B-%Y')
        Recent_Invoices =  Transaction_Table.objects.order_by('Collection_Date').filter(Q(Collection_Date__year=start_date_object.year, Collection_Date__month=start_date_object.month),Q(Active_Flag=True),Q(Updated_User=request.user))
       
        Sum_Dict = {'TIL1_Card':Recent_Invoices.aggregate(Sum('TIL1_Card')).values()[0],
                    'TIL1_Cash':Recent_Invoices.aggregate(Sum('TIL1_Cash')).values()[0],
                    'TIL1_Total': Recent_Invoices.aggregate(Sum('TIL1_Total')).values()[0],
                    'TIL2_Total':Recent_Invoices.aggregate(Sum('TIL2_Total')).values()[0],
                    'Grand_Total' : Recent_Invoices.aggregate(Sum('Grand_Total')).values()[0],   
		     'Bank_Deposit' : Recent_Invoices.aggregate(Sum('Bank_Deposit')).values()[0]
                    }
        print Sum_Dict
        return render(request, 'Retail_Report/Invoice_report_custom_ajax.html', {'Sum_Dict':Sum_Dict,"my_invoices_qs" :Recent_Invoices,'start_date_object':start_date_object ,'start_date':start_data})

def Custom_sales_report_Auditor(request):
    if request.POST:
        start_data = str((request.POST['startdate'])).lstrip().rstrip()
        print start_data
        start_date_object = datetime.strptime(start_data,'%B-%Y')
        Recent_Invoices =  Transaction_Table.objects.order_by('Collection_Date').filter(Q(Collection_Date__year=start_date_object.year, Collection_Date__month=start_date_object.month),Q(Active_Flag=True),Q(Updated_User=request.user))
       
        Sum_Dict = {'TIL1_Card':Recent_Invoices.aggregate(Sum('TIL1_Card')).values()[0],
                    'TIL1_Cash':Recent_Invoices.aggregate(Sum('TIL1_Cash')).values()[0],
                    'TIL1_Total': Recent_Invoices.aggregate(Sum('TIL1_Total')).values()[0],
    
                    }
        print Sum_Dict
        return render(request, 'Retail_Report/Invoice_report_custom_AJAX_Auditor.html', {'Sum_Dict':Sum_Dict,"my_invoices_qs" :Recent_Invoices,'start_date_object':start_date_object ,'start_date':start_data})
    
    


def Print_Report(request,month,year):
    start_date = str(month) + '-' + str(year)
    start_date_object = datetime.strptime(start_date,'%B-%Y')
    my_invoices_qs = Transaction_Table.objects.order_by('Collection_Date').filter(Q(Collection_Date__year=start_date_object.year, Collection_Date__month=start_date_object.month) ,Q(Active_Flag=True),Q(Updated_User=request.user))
    Total_Til1_Card = my_invoices_qs.aggregate(Sum('TIL1_Card')).values()[0]
    type(Total_Til1_Card)
    Total_TIL1_Cash = my_invoices_qs.aggregate(Sum('TIL1_Cash'))
    Total_TIL1_Total = my_invoices_qs.aggregate(Sum('TIL1_Total'))
    Total_TIL2_Total = my_invoices_qs.aggregate(Sum('TIL2_Total'))
    Total_Grand_Total = my_invoices_qs.aggregate(Sum('Grand_Total'))
   
    Sum_Dict = {'TIL1_Card':my_invoices_qs.aggregate(Sum('TIL1_Card')).values()[0],
                'TIL1_Cash':my_invoices_qs.aggregate(Sum('TIL1_Cash')).values()[0],
                'TIL1_Total': my_invoices_qs.aggregate(Sum('TIL1_Total')).values()[0],
                'TIL2_Total':my_invoices_qs.aggregate(Sum('TIL2_Total')).values()[0],
                'Grand_Total' : my_invoices_qs.aggregate(Sum('Grand_Total')).values()[0],        
		'Bank_Deposit' :  my_invoices_qs.aggregate(Sum('Bank_Deposit')).values()[0]
                }

    
    return render(request, 'Retail_Report/print_invoice.html', { 'start_date_object':start_date_object , 'my_invoices_qs':my_invoices_qs, 'Sum_Dict':Sum_Dict})


def Print_Report_Auditor(request,month,year):
    start_date = str(month) + '-' + str(year)
    start_date_object = datetime.strptime(start_date,'%B-%Y')
    my_invoices_qs = Transaction_Table.objects.order_by('Collection_Date').filter(Q(Collection_Date__year=start_date_object.year, Collection_Date__month=start_date_object.month) ,Q(Active_Flag=True),Q(Updated_User=request.user))

   
    Sum_Dict = {'TIL1_Card':my_invoices_qs.aggregate(Sum('TIL1_Card')).values()[0],
                'TIL1_Cash':my_invoices_qs.aggregate(Sum('TIL1_Cash')).values()[0],
                'TIL1_Total': my_invoices_qs.aggregate(Sum('TIL1_Total')).values()[0],    
                }

    
    return render(request, 'Retail_Report/print_invoice_Auditor.html', { 'start_date_object':start_date_object , 'my_invoices_qs':my_invoices_qs, 'Sum_Dict':Sum_Dict})



    

class WorkoutCalendar(HTMLCalendar):
    def __init__(self, workouts):
        super(WorkoutCalendar, self).__init__()
        self.workouts = self.group_by_day(workouts)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.workouts:
                if len(self.workouts[day]) > 1:
                    cssclass += ' Duplicate'
                else:
                    cssclass += ' filled'
                body = []
                for workout in self.workouts[day]:

                    body.append('<button type="button" class="btn" data-toggle="modal" data-target="#myModal" data-remote="/Retail_Report/get_record/%s">' %workout.id)
                    body.append(esc(workout.TIL1_Total))
                    body.append('</button>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(WorkoutCalendar, self).formatmonth(year, month)

    def group_by_day(self, workouts):
        field = lambda workout: workout.Collection_Date.day
        return dict(
            [(day, list(items)) for day, items in groupby(workouts, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)


def Monthly_Report(request):
    start_date = str((request.POST['startdate'])).lstrip().rstrip()
    start_date_object = datetime.strptime(start_date,'%B-%Y')
    
    if request.POST:
        my_workouts = Transaction_Table.objects.order_by('Collection_Date').filter(Q
            (Collection_Date__year=int(start_date_object.year), Collection_Date__month=int(start_date_object.month)),Q(Active_Flag=True),Q(Updated_User=request.user)
          )
        Total_Til1_Card = my_workouts.aggregate(Sum('TIL1_Card')).values()[0]
        type(Total_Til1_Card)
        Total_TIL1_Cash = my_workouts.aggregate(Sum('TIL1_Cash'))
        Total_TIL1_Total = my_workouts.aggregate(Sum('TIL1_Total'))
        Total_TIL2_Total = my_workouts.aggregate(Sum('TIL2_Total'))
        Total_Grand_Total = my_workouts.aggregate(Sum('Grand_Total'))
       
        Sum_Dict = {'TIL1_Card':my_workouts.aggregate(Sum('TIL1_Card')).values()[0],
                    'TIL1_Cash':my_workouts.aggregate(Sum('TIL1_Cash')).values()[0],
                    'TIL1_Total': my_workouts.aggregate(Sum('TIL1_Total')).values()[0],
                    'TIL2_Total':my_workouts.aggregate(Sum('TIL2_Total')).values()[0],
                    'Grand_Total' : my_workouts.aggregate(Sum('Grand_Total')).values()[0]        
                    }
        
        cal = WorkoutCalendar(my_workouts).formatmonth(int(start_date_object.year), int(start_date_object.month))
        return render_to_response('Retail_Report/Monthly_Calender_ajax.html', {'Total_Til1_Card' : Total_Til1_Card,'calendar': mark_safe(cal), "start_date" : start_date})


def get_record(request,Record_id):
    Trans_Record = Transaction_Table.objects.filter(pk=Record_id)
    print Trans_Record
    return render(request, 'Retail_Report/get_record.html', { 'Trans_Record':Trans_Record})
    
    

def Delete_Record(request,Record_id):
    
    Trans_Record = Transaction_Table.objects.get(id=Record_id)
    try:
        Trans_Record.Active_Flag=False
        Trans_Record.save()
        print "Delete Successful"
    except:
        print "Delete record Failed"
    return HttpResponseRedirect("/Retail_Report/update")



def default(request):
    template = loader.get_template('Retail_Report/events.html')
    context = RequestContext(request)
    context['form'] = Transaction_Form(initial={'Updated_User': request.user,'Active_Flag':True})
    return HttpResponse(template.render(context))

# Create your views here.

def create_event(request):
    print 'Create Event method called'
    today = date.today()
    user=request.user
    if request.method == 'POST':
        today = date.today()
        print 'request.post'
        print request.POST
        TIL1_Cash = float(request.POST['TIL1_Cash'])
        TIL1_Card = float(request.POST['TIL1_Card'])
                          
        TIL1_Total = float(request.POST['TIL1_Total'])
        TIL2_Cash =  float(request.POST['TIL2_Cash'])
        TIL2_Total = float(request.POST['TIL2_Total'])
        start_date =  request.POST['start_date']
        Bank_Deposit = float(request.POST['Bank_Deposit'])
        
        Til_Entry = Transaction_Table(TIL1_Total=TIL1_Total,
                                      TIL2_Total=TIL2_Total,
                                      TIL1_Card=TIL1_Card ,
                                      TIL1_Cash=TIL1_Cash,
                                      Collection_Date=datetime.strptime(start_date, '%Y-%m-%d'),
                                      Updated_User=user,
                                      Active_Flag =True,
                                      Bank_Deposit=Bank_Deposit
                                      )
        
        print Til_Entry
                                      
        Til_Entry.save()
        
        
        return HttpResponse('Event Updated Successfully') 



def get_events(request):

    start_date = request.GET.get('start')
    End_date = request.GET.get('end')
    
    events_qs = Transaction_Table.objects.filter(Q(Collection_Date__range=[start_date, End_date]),Q(Active_Flag=True),Q(Updated_User=request.user))
    
    event_json = []
    
    
    for event in events_qs:
        
        event_dict={
                'id' : event.id,
                'title': str(event.Grand_Total),
                 #'start' : event.Collection_Date.strftime("new Date(%Y, %m, %d"),
                 'start' : event.Collection_Date.strftime("%Y-%m-%dT%H:%M:%S"),
                'className': 'label-important',
                'allDay' : True
                }
        event_json.append(event_dict)
            
    
    
    """
    [
          {
            title: 'All Day Event',
            start: new Date(y, m, 1),
            className: 'label-important'
          },
    ]
    """
    print event_json
    #return JsonResponse(event_json, safe=False)
    return HttpResponse(json.dumps(event_json), content_type='application/json')

def remove_event(request):
    Record_id = request.POST['event_id']
    print Record_id
    Trans_Record = Transaction_Table.objects.get(id=Record_id)
    try:
        Trans_Record.Active_Flag=False
        Trans_Record.save()
        print "Delete Successful"
        Send_Response = "Entry Deleted Successfully"
    except:
        print "Delete record Failed"
        Send_Response = "Entry Deletion Failed"
    return HttpResponse(Send_Response)
    
