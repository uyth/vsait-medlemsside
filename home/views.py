from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views import generic
from django.conf import settings 
from django.core.mail import send_mail 

from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site

from .forms import LoginForm, VsaitUserRegistrationForm, VsaitUserProfileChangeForm, VsaitUserFoodNeedsChangeForm, VsaitUserIsStudent, ResetPasswordForm
from events.models import Event
from home.models import VsaitUser
import uuid

# @login_required
def index(request):
    context = {}
    form = LoginForm(data = request.POST)
    if request.method == "POST":
        # Alert membership
        print(request.POST)
        if "alert_membership" in request.POST.keys():
            request.user.alert_membership_read = True
            request.user.save()
            redirect("/")
        else:
            # Login form
            if form.is_valid():
                user = form.get_user()
                if (user):
                    if (user.email_confirmed):
                        login(request,user)
                    else:
                        messages.error(request, 'Please confirm email before loggin in!')
        # redirects back to event page if found ?next=
        referer_link = request.POST.get('next', '/')
        if (referer_link == ""): # If nothing, redirect login to homepage
            referer_link = "/"
        return redirect(referer_link)
    context['form'] = form
    context["events"] = Event.objects.filter(endTime__gte=timezone.now()).order_by('-startTime')[::-1]
    context["pending_events"] = []
    context["attending_events"] = []
    context['get_year'] = str((timezone.now().year)-1)+" / "+str(timezone.now().year)
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
    if request.user.is_authenticated:
            return redirect('/')
    context = {}
    form = VsaitUserRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            # login(request,user)
            messages.success(request, 'Your account was successfully created!')
            # Mail
            current_site = get_current_site(request)
            subject = 'Welcome to VSAIT'
            message = f'Hi {user.firstname}, thank you for registering as a VSAIT user.\nPlease click on the link to confirm your email: http://{current_site}/activate/{user.secret_email_confirmation_url}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ] 
            send_mail( subject, message, email_from, recipient_list )
            # return redirect('/')
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
    context['memberships'] = list(request.user.memberships.all())[1:]
    context['form_is_student'] = VsaitUserIsStudent(user=request.user)
    # Formchange password
    if request.method == 'POST':
        if "food_needs" in list(request.POST.keys()):
            form_food_needs = VsaitUserFoodNeedsChangeForm(request.POST, user=request.user)
            food_needs = form_food_needs.data.get("food_needs")
            request.user.food_needs = food_needs
            request.user.save()
            return HttpResponseRedirect(reverse('home:profile'))
        elif "is_student_2" in list(request.POST.keys()):
            form_is_student = VsaitUserIsStudent(request.POST, user=request.user)
            is_student = form_is_student.data.get("is_student")
            is_student = True if is_student else False
            request.user.student = is_student
            request.user.save()
            return HttpResponseRedirect(reverse('home:profile'))
        else:
            form_password = PasswordChangeForm(request.user, request.POST)
            print(form_password.is_valid())
            if form_password.is_valid():
                user = form_password.save()
                print(user,request)
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return HttpResponseRedirect(reverse('home:profile'))
            else:
                messages.error(request, 'Please correct the error below.')
    form_password = PasswordChangeForm(request.user)
    form_food_needs = VsaitUserFoodNeedsChangeForm(user=request.user)
    context['form_password'] = form_password
    context['form_food_needs'] = form_food_needs
    return render(request,'home/profile.html',context)

@login_required()
def statistics(request):
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
    return render(request,'home/statistics.html',context)

def pendingMembership(request):
    request.user.pending_membership = not request.user.pending_membership
    request.user.save()
    return HttpResponseRedirect(reverse('home:profile'))

def kontakt(request):
    context = {}
    #context['user'] = request.user
    #print(VsaitUser.objects.all().values())
    return render(request,'home/contact.html',context)

def activate(request, secret_url):
    if request.user.is_authenticated:
            return redirect('/')
    context = {}
    user = get_object_or_404(VsaitUser, secret_email_confirmation_url=secret_url)
    user.secret_email_confirmation_url = uuid.uuid4().hex
    user.email_confirmed = True
    user.save()
    #login(request,user)
    #return redirect('/')
    return render(request, 'home/activate.html',context)

def forgot_password(request):
    if request.user.is_authenticated:
            return redirect('/')
    context = {}
    if request.method == "POST":
        if "email" in request.POST.keys():
            user = get_object_or_404(VsaitUser, email=request.POST.get("email"))
            user.secret_password_change_url = uuid.uuid4().hex
            user.save()
            # Mail
            subject = '[VSAIT] Reset your password'
            current_site = get_current_site(request)
            message = f'Hi {user.firstname}, you have registered that your password was forgotten.\nPlease click on the link to change your password: http://{current_site}/reset_password/{user.secret_password_change_url}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ] 
            send_mail( subject, message, email_from, recipient_list )
    return render(request, 'home/forgot_password.html',context)

def reset_password(request, secret_url):
    if request.user.is_authenticated:
            return redirect('/')
    context = {}
    user = get_object_or_404(VsaitUser, secret_password_change_url=secret_url)
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            password = form.data.get("password")
            password_confirmation = form.data.get("password_confirmation")
            if password == password_confirmation:
                user.set_password(password)
                user.secret_password_change_url = uuid.uuid4().hex
                user.save()
                return render(request, 'home/reset_password_success.html')
    form = ResetPasswordForm(request.POST)
    context["form"] = form
    return render(request, 'home/reset_password.html', context)
