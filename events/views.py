from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from .models import Event

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'events'
    paginate_by = 5

    def get_queryset(self):
        now = timezone.now()
        #upcoming_events = Event.objects.filter(startTime__gte=now).order_by('-startTime')[::-1]
        
        ongoing_events = Event.objects.filter(endTime__gte=now).order_by('-startTime')[::-1]
        events = list(Event.objects.filter(startTime__lt=now).order_by('-startTime'))
        #return upcoming_events + events
        return ongoing_events + events
   
class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        event = get_object_or_404(Event, id=self.kwargs['pk'])
        data["is_registered"] = event.registrations.filter(id=self.request.user.id).exists()
        data["is_waiting"] = event.waiting_list.filter(id=self.request.user.id).exists()
        data["can_register"] = event.ontime_for_registration_deadline()
        data["can_cancel"] = event.ontime_for_cancellation_deadline()
        return data

def EventRegistration(request, pk):
    event = get_object_or_404(Event, id=request.POST.get('event_id'))
    # Does nothing if event startTime has passed
    if event.is_upcoming():
        # Event type is member and user is not member, then skip, else go through as normal
        if event.event_type == "medlem" and not request.user.membership:
            print(request.user,request.user.membership)
            messages.error(request, 'Membership is required to register this event!')
            pass
        elif event.registrations.filter(id=request.user.id).exists() and event.ontime_for_cancellation_deadline(): 
            event.registrations.remove(request.user) # Check if user is registered, remove if true
        elif not event.is_full() and event.ontime_for_registration_deadline():
            event.registrations.add(request.user) # Check for fullness, if not full adds user to registrations
        elif event.waiting_list.filter(id=request.user.id).exists():
            event.waiting_list.remove(request.user) # If user already in waiting list, remove
        else:
            event.waiting_list.add(request.user) # If user is not in waiting list nor in registration, add to waiting list
        update_waiting_list(event)
    return HttpResponseRedirect(reverse('events:detail', args=[str(pk)]))

# Waiting list update function
def update_waiting_list(event):
    # Checks if there's spot on the event, loop through the waiting list then add the user
    print(event.waiting_list.all())
    for user in list(event.waiting_list.all()):
        if event.number_of_registrations() < event.max_people:
            event.registrations.add(user)
            event.waiting_list.remove(user)
