from django.shortcuts import render
from .models import Event

def home(request):
    events = Event.objects.filter(is_published=True)
    return render(request, "home.html", {
        "events": events
    })
