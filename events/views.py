from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import JsonResponse
from Retail_Report.models import Transaction_Table
import json
from django.db.models import Q
from datetime import date,datetime
from Retail_Report.forms import Transaction_Form



def index(request):
    template = loader.get_template('events/events.html')
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
    'http://dev.kmine.com:8001/mysite?start=2016-03-27&end=2016-05-08&_=1458774645111'
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