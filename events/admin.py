from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'pub_date', 'is_upcoming')
    list_filter = ['pub_date']

admin.site.register(Event)
