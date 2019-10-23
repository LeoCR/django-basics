from django.shortcuts import render
from django.http import HttpResponse
from django_app.models import Topic,Webpage,AccessRecord
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records':webpages_list
    }
    return render(request,'app/index.html',context=date_dict)

def content(request):
    temp_dict={
        'content':"Hello I am a Django Content"
    }
    return render(request,'app/main.html',context=temp_dict)