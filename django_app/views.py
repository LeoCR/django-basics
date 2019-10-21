from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    temp_dict={'django_variable':"I am a Django Variable"}
    return render(request,'app/index.html',context=temp_dict)