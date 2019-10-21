from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    temp_dict={
        'django_variable':"I am a Django Variable injected"
    }
    return render(request,'app/index.html',context=temp_dict)

def content(request):
    temp_dict={
        'content':"Hello I am a Django Content"
    }
    return render(request,'app/main.html',context=temp_dict)