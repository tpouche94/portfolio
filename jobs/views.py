from django.shortcuts import render
from .models import Job

jobs = Job.objects


def home(request):
    return render(request, 'home.html', {'jobs': jobs})