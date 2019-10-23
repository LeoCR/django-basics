import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()

import random
from django_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']