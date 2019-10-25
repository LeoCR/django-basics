from django_app import views
from django.urls import path
app_name = 'app'
urlpatterns=[
    path('',views.index,name='home'),
    path('users/',views.users,name='users'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]