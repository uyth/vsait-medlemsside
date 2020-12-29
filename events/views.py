from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from .models import Event

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'events'
    paginate_by = 3

    def get_queryset(self):
        now = timezone.now()
        upcoming_events = Event.objects.filter(startTime__gte=now).order_by('-startTime')[::-1]
        events = list(Event.objects.filter(startTime__lt=now).order_by('-startTime'))
        return upcoming_events + events
   
class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        event = get_object_or_404(Event, id=self.kwargs['pk'])
        registered = False
        if event.registrations.filter(id=self.request.user.id).exists():
            registered = True
        data["is_registered"] = registered
        data["can_register"] = event.is_upcoming()
        return data

def EventRegistration(request, pk):
    event = get_object_or_404(Event, id=request.POST.get('event_id'))
    if event.is_upcoming():
        if event.registrations.filter(id=request.user.id).exists():
            event.registrations.remove(request.user)
        else:
            event.registrations.add(request.user)
    return HttpResponseRedirect(reverse('events:detail', args=[str(pk)]))
