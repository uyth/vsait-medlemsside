from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import generic

from .forms import LoginForm, VsaitUserRegistrationForm
from events.models import Event

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
    context["events"] = Event.objects.filter(startTime__gte=timezone.now())
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
