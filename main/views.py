from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View
# from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm

from .models import Coaches, Directions

# Create your views here.

def index(request):
    coaches = Coaches.objects.all()
    directions = Directions.objects.all()
    context = {
        "coach_list": coaches,
        "direction_list": directions
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')

def CoachesView(request):
    coaches = Coaches.objects.all()
    return render(request, "main/index.html", {"coach_list": coaches})

def DirectionsView(request):
    directions = Directions.objects.all()
    return render(request, "main/index.html", {"direction_list": directions})