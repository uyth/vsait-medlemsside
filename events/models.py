from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

from home.models import VsaitUser

TYPE_CHOICES = [
    ("medlem","Membership required"),
    ("alle","Open for all"),
]
class Event(models.Model):
    title = models.CharField(max_length=200)
    # description = models.CharField(max_length=200)
    description = HTMLField()
    # image_link = models.CharField(max_length=200)
    # image = models.ImageField()
    image = models.ImageField(upload_to='event_uploads', default='default_event_image.jpg')

    startTime = models.DateTimeField('startTime')
    endTime = models.DateTimeField('endTime')
    registrationDeadline = models.DateTimeField('Registration deadline')
    cancellationDeadline = models.DateTimeField('Cancellation deadline')
    location = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="medlem")

    max_people = models.IntegerField()
    registrations = models.ManyToManyField(VsaitUser, related_name='registrations', blank=True)
    waiting_list = models.ManyToManyField(VsaitUser, related_name="waiting_list", blank=True)

    last_edited = models.DateTimeField('date last edited', auto_now=True)
    is_draft = models.BooleanField(default=False)
    draft_publish_time = models.DateTimeField('draft_publish_time',default=timezone.now, blank=True)
    def __str__(self):
        return self.title
    def number_of_registrations(self):
        return self.registrations.count()
    def number_of_waiting_users(self):
        return self.waiting_list.count()
    # Time related
    def is_upcoming(self):
        return self.startTime >= timezone.now()
    def is_ongoing(self):
        return self.endTime >= timezone.now()
    def ontime_for_registration_deadline(self):
        return self.registrationDeadline >= timezone.now()
    def ontime_for_cancellation_deadline(self):
        return self.cancellationDeadline >= timezone.now()
    def is_full(self):
        return self.registrations.count() >= self.max_people
    def has_waiting_users(self):
        return self.waiting_list.count() > 0
    is_upcoming.admin_order_field = 'upcoming'
    is_upcoming.boolean = True
    is_upcoming.short_description = 'Upcoming events'

