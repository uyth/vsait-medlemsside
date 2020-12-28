from django.contrib import admin
from .models import Event
from index.models import CustomUser
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['event_name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('event_name', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Event)
