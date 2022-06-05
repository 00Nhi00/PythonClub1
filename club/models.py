from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Meeting(models.Model):
  meetingid=models.AutoField(primary_key=True)
  meetingtitle=models.CharField(max_length=225)
  meetingdate=models.DateField()
  meetingtime=models.TimeField()
  meetinglocation=models.CharField(max_length=225)
  agenda=models.TextField()

  def __str__(self):
    return self.meetingtitle

  class Meta:
    db_table='meeting'

class MeetingMinute(models.Model):
  meetingid=models.ForeignKey(Meeting, on_delete=models.CASCADE) 
  attendance=models.ManyToManyField(User)
  minutestext=models.TextField()

  def __str__(self):
    return self.meetingid

  class Meta:
    db_table='meetingminute'

class Resource(models.Model):
  resourcename=models.CharField(max_length=225)
  resourcetype=models.CharField(max_length=225)
  resourceURL=models.URLField(null=True, blank=True)
  dateentered=models.DateField()
  userid=models.ForeignKey(User, on_delete=models.CASCADE)
  resourcedescription=models.TextField()

  def __str__(self):
    return self.resourcename
  
  class Meta:
    db_table='resource'

class Event(models.Model):
  eventtitle=models.CharField(max_length=225)
  eventlocation=models.CharField(max_length=225)
  eventdate=models.DateField()
  eventtime=models.TimeField()
  eventdescription=models.TextField(null=True, blank=True)
  userid=models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.eventtitle

  class Meta:
    db_table='event'


