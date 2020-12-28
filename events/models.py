from django.db import models
from django.utils import timezone
import datetime

from index.models import CustomUser

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = models.CharField(max_length=200)
    event_image_link = models.CharField(max_length=200)

    #event_startTime = models.CharField(max_length=200)
    #event_endTime = models.CharField(max_length=200)
    event_startTime = models.DateTimeField('startTime')
    event_endTime = models.DateTimeField('endTime')
    event_location = models.CharField(max_length=200)

    event_max_people = models.CharField(max_length=200)
    registrations = models.ManyToManyField(CustomUser, related_name='registrations', blank=True)

    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.event_name
    def number_of_registrations(self):
        return self.registrations.count()
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def is_upcoming(self):
        now = timezone.now()
        return self.event_startTime >= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

datetime.timedelta(days=1)
