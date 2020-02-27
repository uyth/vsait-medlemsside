from django.views import generic

from .models import Event


class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'current_events'

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.order_by('-published')[:5]


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
