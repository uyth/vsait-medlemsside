from django.db import models
from django.utils import timezone

from home.models import VsaitUser

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200)
    #image = models.ImageField()

    startTime = models.DateTimeField('startTime')
    endTime = models.DateTimeField('endTime')
    location = models.CharField(max_length=200)

    max_people = models.IntegerField()
    registrations = models.ManyToManyField(VsaitUser, related_name='registrations', blank=True)
    waiting_list = models.ManyToManyField(VsaitUser, related_name="waiting_list", blank=True)

    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    def number_of_registrations(self):
        return self.registrations.count()
    def number_of_waiting_users(self):
        return self.waiting_list.count()
    def is_upcoming(self):
        now = timezone.now()
        return self.startTime >= now
    def is_full(self):
        return self.registrations.count() >= self.max_people
    def has_waiting_users(self):
        return self.waiting_list.count() > 0
    is_upcoming.admin_order_field = 'upcoming'
    is_upcoming.boolean = True
    is_upcoming.short_description = 'Upcoming events'

