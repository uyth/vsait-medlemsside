from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import LoginForm, CustomUserRegistrationForm
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
        #return render(request, 'index/index.html',context)
        return redirect('/')
    context['form'] = form
    #context["events"] = Event.objects.all()
    context["events"] = Event.objects.filter(event_startTime__gte=timezone.now())
    return render(request, 'index/index.html',context)

def sign_up(request):
    context = {}
    form = CustomUserRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    context['form'] = form
    return render(request,'index/signup.html',context)
