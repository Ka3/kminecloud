from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import JsonResponse
from Retail_Report.models import Transaction_Table
import json



def index(request):
    template = loader.get_template('events/events.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

# Create your views here.




def get_events(request):
    'http://dev.kmine.com:8001/mysite?start=2016-03-27&end=2016-05-08&_=1458774645111'
    start_date = request.GET.get('start')
    End_date = request.GET.get('end')
    
    events_qs = Transaction_Table.objects.filter(Collection_Date__range=[start_date, End_date])
    
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