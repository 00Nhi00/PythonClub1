from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinute, Resource, Event
import datetime
# Create your tests here.
class MeetingTest(TestCase):
  def setUp(self):
    self.title=Meeting(meetingtitle='1st meeting')
    self.date=Meeting(meetingdate='(6/2/2022)')
  def test_meetingstring(self):
    self.assertEqual(str(self.title), '1st meeting')
  def test_tablename(self):
    self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinuteTest(TestCase):
  def setUp(self):
    self.meetingid=Meeting(meetingid='1')
    self.attendance=MeetingMinute(atttendance='user1')
    self.minutestext=MeetingMinute(minutestext='text1')
    self.meetingminute=MeetingMinute(meetingid='1', attedance=self.attendace, minutestext=self.minutestext)
  def test_meetingminutestring(self):
    self.assertEqual(str(self.minutestext), 'text 1')

class ResourceTest(TestCase):
  def setUp(self):
    self.resourcename=Resource(resourcename='Financial Forms')
    self.resourcetype=Resource(resourcetype='forms')
    self.resouceURL=Resource(resourceURL='resource.com')
    self.dateentered=Resource(dateentered='6/2/2022')
    
  def test_resourcestring(self):
    self.assertEqual(str(self.resourcename),'Financial Form')

class EventTest(TestCase):
  def setUp(self):
    self.eventtitle=Event(eventtitle="Python Coding")
    self.eventlocation=Event(eventlocation="122nd Ave, Seattle, 98122")
  
  def test_eventstring(self):
    self.assertEqual(str(self.event), 'Python Coding')