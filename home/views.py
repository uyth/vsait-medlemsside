from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import generic

from .forms import LoginForm, VsaitUserRegistrationForm
from events.models import Event
from home.models import VsaitUser

# @login_required
def index(request):
    context = {}
    form = LoginForm(data = request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            if (user):
                login(request,user)
        return redirect('/')
    context['form'] = form
    context["events"] = Event.objects.filter(startTime__gte=timezone.now()).order_by('-startTime')[::-1]
    # Filters out draft event, updates draft event if it's time for publish date
    for event in context["events"]:
        if event.is_draft:
            if event.draft_publish_time <= timezone.now():
                print("AAA")
                event.is_draft = False;
                event.save()
            else:
                print(event.draft_publish_time, timezone.now())
                context["events"].remove(event)
    return render(request, 'home/index.html',context)

def sign_up(request):
    context = {}
    form = VsaitUserRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    context['form'] = form
    return render(request,'home/signup.html',context)

@login_required()
def profile(request):
    context = {}
    context['user'] = request.user
    print(VsaitUser.objects.all().values())
    return render(request,'home/profile.html',context)


def kontakt(request):
    context = {}
    #context['user'] = request.user
    #print(VsaitUser.objects.all().values())
    return render(request,'home/contact.html',context)
