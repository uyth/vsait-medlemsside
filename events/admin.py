from django.contrib import admin
from .models import Event
from .forms import EventForm, EventChangeForm

class EventAdmin(admin.ModelAdmin):
    add_form = EventForm # Add new user form
    form = EventChangeForm # Edit user form
    list_display = ('title', 'startTime', 'endTime', 'last_edited', 'is_upcoming','is_draft')
    list_filter = ['last_edited','startTime','is_draft']
    search_fields = ('title',)
    ordering = ('startTime',)
    filter_horizontal = ()

    fieldsets = (
        (None,               {'fields': ['title','description','image','location','max_people','event_type']}),
        ('Date information', {'fields': ['startTime','endTime','registrationDeadline','cancellationDeadline',]}),
        ('Registration information', {'fields': ['registrations'], 'classes': ['collapse']}),
        ('Waiting list information', {'fields': ['waiting_list'], 'classes': ['collapse']}),
        ('Checkin/attendance information', {'fields': ['secret_url','attendance'], 'classes': ['collapse']}),
        (None,               {'fields': ['is_draft','draft_publish_time']}),
    )
    add_fieldsets = (
        (None,               {'fields': ['title','description','image','location','max_people','event_type']}),
        ('Date information', {'fields': ['startTime','endTime','registrationDeadline','cancellationDeadline',]}),
        ('Registration information', {'fields': ['registrations'], 'classes': ['collapse']}),
        ('Waiting list information', {'fields': ['waiting_list'], 'classes': ['collapse']}),
        ('Checkin/attendance information', {'fields': ['secret_url','attendance'], 'classes': ['collapse']}),
        (None,               {'fields': ['is_draft','draft_publish_time']}),
    )

    # Removes the default delete action
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        """ Hides draft publish time if event is not a draft
        if not obj.is_draft:
            print(obj.__dict__)
            self.exclude.append('draft_publish_time')
        """
        self.exclude.append('last_edited')
        return super(EventAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Event, EventAdmin)
