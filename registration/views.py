from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

from .forms import RegistrationForm 

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/registration.html', 
		{
		'title': 'Registrer bruker',
		'form': form
		}
	)