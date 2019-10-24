from django.contrib import admin
from django_app.models import User,AccessRecord,Topic,Webpage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)
# Register your models here.
