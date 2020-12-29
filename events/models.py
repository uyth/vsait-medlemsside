from django.db import models
from django.utils import timezone

from home.models import VsaitUser

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200)

    startTime = models.DateTimeField('startTime')
    endTime = models.DateTimeField('endTime')
    location = models.CharField(max_length=200)

    max_people = models.CharField(max_length=200)
    registrations = models.ManyToManyField(VsaitUser, related_name='registrations', blank=True)

    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.event_name
    def number_of_registrations(self):
        return self.registrations.count()
    def is_upcoming(self):
        now = timezone.now()
        return self.event_startTime >= now
    is_upcoming.admin_order_field = 'upcoming'
    is_upcoming.boolean = True
    is_upcoming.short_description = 'Upcoming events'

