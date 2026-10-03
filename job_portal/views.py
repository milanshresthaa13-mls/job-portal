from django.shortcuts import render


def home(request):
    return render(request, 'landing/home.html')


def job_seekers(request):
    return render(request, 'landing/job_seekers.html')


def employers(request):
    return render(request, 'landing/employers.html')
