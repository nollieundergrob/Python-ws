from django.db import models
import datetime
# Create your models here.
class Attendance(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    student = models.CharField(max_length=100)
    date_check = models.CharField(default=str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M")),max_length=100)
