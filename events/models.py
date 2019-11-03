from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(default=None, blank=True, null=True)
    place = models.CharField(max_length=255)
    register_attendance_required = models.BooleanField(default=True)
    published = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
