from django.shortcuts import render
from django.http import HttpResponse
from django_app.models import Topic,Webpage,AccessRecord
from . import forms
from django_app.forms import NewUserForm
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records':webpages_list
    }
    return render(request,'app/index.html',context=date_dict)
def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request,'app/form_page.html',{'form':form})
def content(request):
    temp_dict={
        'content':"Hello I am a Django Content"
    }
    return render(request,'app/main.html',context=temp_dict)

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'app/users.html',{'form':form})
def other(request):
    return render(request,'app/other.html')
def relative(request):
    return render(request,'app/relative_url_templates.html')