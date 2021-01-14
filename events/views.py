from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

from .models import Event
from home.models import VsaitUser

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'events'
    paginate_by = 5

    def get_queryset(self):
        now = timezone.now()
        #upcoming_events = Event.objects.filter(startTime__gte=now).order_by('-startTime')[::-1]
        
        ongoing_events = Event.objects.filter(endTime__gte=now).order_by('-startTime')[::-1]
        events = list(Event.objects.filter(endTime__lt=now).order_by('-startTime'))
        #return upcoming_events + events
        return ongoing_events + events
   
class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        event = get_object_or_404(Event, id=self.kwargs['pk'])
        # User information
        data["is_registered"] = event.registrations.filter(id=self.request.user.id).exists()
        data["is_waiting"] = event.waiting_list.filter(id=self.request.user.id).exists()
        if data['is_waiting']:
            data['waiting_number'] = [x.email for x in event.waiting_list.all()].index(self.request.user.email)+1
        data["can_register"] = event.ontime_for_registration_deadline()
        data["can_cancel"] = event.ontime_for_cancellation_deadline()
        # Display users
        information = [{'name':x.firstname+" "+x.lastname, 'email':x.email,'anonymous':x.anonymous_display, 'display':""} for x in event.registrations.all()]
        for user in information:
            if user.get("anonymous"):
                user.update({"display":"Anonymous"})
            else:
                user.update({"display":user.get("name")+" ; "+user.get("email")})
        data["display_users"] = information
        # Staffs information
        food_needs_information = [{'email':x.email, 'name':x.firstname+" "+x.lastname, 'food_needs':x.food_needs} for x in event.registrations.all()]
        data["food_needs_information"] = food_needs_information
        return data

def EventRegistration(request, pk):
    event = get_object_or_404(Event, id=request.POST.get('event_id'))
    # Does nothing if event startTime has passed
    print(event.event_type, request.user.has_membership_boolean(), request.user.pending_membership)
    if event.is_upcoming():
        # Event type is member and user is not member, then skip, else go through as normal
        if event.event_type == "medlem" and not request.user.has_membership_boolean() and not request.user.pending_membership:
            messages.error(request, 'Membership is required to register this event!')
            pass
        elif event.registrations.filter(id=request.user.id).exists() and event.ontime_for_cancellation_deadline(): 
            print("remove")
            event.registrations.remove(request.user) # Check if user is registered, remove if true
        elif not event.is_full() and event.ontime_for_registration_deadline():
            print("add")
            event.registrations.add(request.user) # Check for fullness, if not full adds user to registrations
        elif event.waiting_list.filter(id=request.user.id).exists():
            print("remove2")
            event.waiting_list.remove(request.user) # If user already in waiting list, remove
        else:
            print(event.is_full(), event.ontime_for_registration_deadline())
            print("add2")
            event.waiting_list.add(request.user) # If user is not in waiting list nor in registration, add to waiting list
        update_waiting_list(event)
    return HttpResponseRedirect(reverse('events:detail', args=[str(pk)]))

def CheckIn(request, pk, secret_url):
    context = {}
    event = get_object_or_404(Event, id=pk)
    print(request.path,pk,secret_url)
    if len(list(request.POST)) > 0:
        email = request.POST.get("email")
        user = VsaitUser.objects.filter(email=email).get()
        # If user is registered, register attendance
        if event.registrations.filter(id=user.id).exists():
            print(user)
            if event.attendance.filter(id=user.id).exists():
                messages.error(request, "Email received has already registered attendance!")
            else:
                event.attendance.add(user)
                messages.success(request, 'The user has successfully registered their attendance!')
        else:
            messages.error(request, "Email received wasn't found in registrations")
    if event.secret_url != secret_url:
        raise Http404("No url matches the given query.")
    # Display users
    attendances = [{'name':x.firstname+" "+x.lastname, 'email':x.email} for x in event.attendance.all()]
    attendances_email = [x['email'] for x in attendances]
    registrations = [{'name':x.firstname+" "+x.lastname, 'email':x.email} for x in event.registrations.all()]
    attended = []
    registered = []
    for user in registrations:
        if user.get('email') in attendances_email:
            user.update({"confirmed": True})
            attended.append(user)
        else:
            user.update({"confirmed": False})
            registered.append(user)
    context["display_users"] = attended + registered
    context['event'] = event
    return render(request,'events/checkin.html',context)

# Waiting list update function
def update_waiting_list(event):
    # Checks if there's spot on the event, loop through the waiting list then add the user
    print(event.waiting_list.all())
    for user in list(event.waiting_list.all()):
        if event.number_of_registrations() < event.max_people:
            event.registrations.add(user)
            event.waiting_list.remove(user)
