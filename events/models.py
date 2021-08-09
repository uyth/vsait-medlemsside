from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
import uuid

from home.models import VsaitUser

TYPE_CHOICES = [
    ("medlem","Membership required"),
    ("alle","Open for all"),
]
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(upload_to='event_uploads', default='default_event_image.jpg')

    startTime = models.DateTimeField('startTime')
    endTime = models.DateTimeField('endTime')
    registrationDeadline = models.DateTimeField('Registration deadline')
    cancellationDeadline = models.DateTimeField('Cancellation deadline')
    location = models.CharField(max_length=200)
    event_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="medlem")

    # registration
    max_people = models.IntegerField()
    registrations = models.ManyToManyField(VsaitUser, related_name='registrations', blank=True)
    waiting_list = models.ManyToManyField(VsaitUser, related_name="waiting_list", blank=True)

    # checkin/attendance
    secret_url = models.CharField(max_length=100, default=uuid.uuid4().hex)
    attendance = models.ManyToManyField(VsaitUser, related_name="attendance", blank=True)

    last_edited = models.DateTimeField('date last edited', auto_now=True)
    is_draft = models.BooleanField(default=False)
    draft_publish_time = models.DateTimeField('draft_publish_time',default=timezone.now, blank=True)
    # Displays
    def __str__(self):
        return self.title
    def number_of_registrations(self):
        return self.registrations.count()
    def number_of_waiting_users(self):
        return self.waiting_list.count()
    def number_of_attendances(self):
        return self.attendance.count()
    def display_max_people(self):
        return self.max_people if self.max_people > 0 else "∞"
    def max_people_unlimited(self):
        return self.max_people == 0
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
        return self.max_people > 0 and self.registrations.count() >= self.max_people
    def has_waiting_users(self):
        return self.waiting_list.count() > 0
    # Admin display
    def last_edited_display(self):
        return self.last_edited.strftime("%d.%b %y, %H:%M")
    def startTime_display(self):
        return self.startTime.strftime("%d.%b %Y, %H:%M")
    def endTime_display(self):
        return self.endTime.strftime("%d.%b %Y, %H:%M")
    last_edited_display.short_description = "last edited"
    last_edited_display.admin_order_field= "last_edited"
    startTime_display.short_description = "start time"
    startTime_display.admin_order_field = "startTime"
    endTime_display.short_description = "end time"
    endTime_display.admin_order_field = "endTime"

    is_upcoming.admin_order_field = 'startTime'
    is_upcoming.short_description = 'upcoming'
    is_upcoming.boolean = True
    is_ongoing.short_description = 'ongoing'
    is_ongoing.boolean = True

