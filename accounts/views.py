from django.contrib.auth import login
from django.shortcuts import render

from .forms import EmployerRegistrationForm, JobSeekerRegistrationForm


def _register(request, form_class, role_name):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'accounts/registration_complete.html', {
                'role_name': role_name,
            })
    else:
        form = form_class()

    return render(request, 'accounts/register.html', {
        'form': form,
        'role_name': role_name,
    })


def register_job_seeker(request):
    return _register(request, JobSeekerRegistrationForm, 'job seeker')


def register_employer(request):
    return _register(request, EmployerRegistrationForm, 'employer')
