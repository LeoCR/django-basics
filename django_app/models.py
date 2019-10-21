from django.db import models

class Topic(models.Model):
    top_name=models.CharField(max_length=240,unique=True)

    def __str__(self):
        return self.top_name
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=240,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
# For run the migrations run this command:  python manage.py makemigrations
# Then run this command:  python manage.py migrate  
# Create your models here.
