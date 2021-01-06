from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import generic

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .forms import LoginForm, VsaitUserRegistrationForm, VsaitUserProfileChangeForm, VsaitUserFoodNeedsChangeForm
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
        # redirects back to event page if found ?next=
        referer_link = request.POST.get('next', '/')
        if (referer_link == ""): # If nothing, redirect login to homepage
            referer_link = "/"
        return redirect(referer_link)
    context['form'] = form
    context["events"] = Event.objects.filter(endTime__gte=timezone.now()).order_by('-startTime')[::-1]
    context["pending_events"] = []
    context["attending_events"] = []
    # Filters out draft event, updates draft event if it's time for publish date
    for event in context["events"]:
        if event.is_draft:
            if event.draft_publish_time <= timezone.now():
                event.is_draft = False;
                event.save()
            else:
                context["events"].remove(event)
        else:
            if event.waiting_list.filter(id=request.user.id).exists():
                context["pending_events"].append(event);
            elif event.registrations.filter(id=request.user.id).exists():
                context["attending_events"].append(event);
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
    # form = VsaitUserProfileChangeForm(request.POST or None)
    context['user'] = request.user
    events = []
    for event in list(Event.objects.all()):
        if (event.registrations.filter(id=request.user.id).order_by('-startTime').exists()):
            events.append(event)
    context['events_count'] = len(events)
    context['events'] = events[::-1]
    context['get_year'] = timezone.now().year

    # Formchange password
    if request.method == 'POST':
        if ("food_needs" in list(request.POST.keys())):
            form_food_needs = VsaitUserFoodNeedsChangeForm(request.POST, user=request.user)
            food_needs = form_food_needs.data.get("food_needs")
            request.user.food_needs = food_needs
            request.user.save()
            # print(request.user.food_needs)
        else:
            form_password = PasswordChangeForm(request.user, request.POST)
            if form_password.is_valid():
                user = form_password.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
    form_password = PasswordChangeForm(request.user)
    form_food_needs = VsaitUserFoodNeedsChangeForm(user=request.user)
    context['form_password'] = form_password
    context['form_food_needs'] = form_food_needs
    return render(request,'home/profile.html',context)

@login_required()
def settings(request):
    context = {}
    # form = VsaitUserProfileChangeForm(request.POST or None)
    context['user'] = request.user
    events = []
    for event in list(Event.objects.all()):
        if (event.registrations.filter(id=request.user.id).order_by('-startTime').exists()):
            events.append(event)
    context['events_count'] = len(events)
    context['events'] = events[::-1]
    context['get_year'] = timezone.now().year

    # Formchange password
    if request.method == 'POST':
        if ("food_needs" in list(request.POST.keys())):
            form_food_needs = VsaitUserFoodNeedsChangeForm(request.POST, user=request.user)
            food_needs = form_food_needs.data.get("food_needs")
            request.user.food_needs = food_needs
            request.user.save()
            # print(request.user.food_needs)
        else:
            form_password = PasswordChangeForm(request.user, request.POST)
            if form_password.is_valid():
                user = form_password.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
    form_password = PasswordChangeForm(request.user)
    form_food_needs = VsaitUserFoodNeedsChangeForm(user=request.user)
    context['form_password'] = form_password
    context['form_food_needs'] = form_food_needs
    return render(request,'home/settings.html',context)

def pendingMembership(request):
    request.user.pending_membership = not request.user.pending_membership
    request.user.save()
    return HttpResponseRedirect(reverse('home:settings'))

def kontakt(request):
    context = {}
    #context['user'] = request.user
    #print(VsaitUser.objects.all().values())
    return render(request,'home/contact.html',context)
