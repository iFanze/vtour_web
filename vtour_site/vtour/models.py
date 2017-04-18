from django.db import models

# Create your models here.


class AlarmInfo(models.Model):
    time = models.DateTimeField(null=True)
    probe_no = models.CharField(max_length=200)
    alarm_data = models.CharField(max_length=200)
    alarm_pics = models.CharField(max_length=500)
    spot_name = models.CharField(max_length=100)
