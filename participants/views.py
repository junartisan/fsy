from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from events.models import Event
from django.utils import timezone

from .models import Participant
from .forms import ParticipantLoginForm


# FRONT PAGE
def home(request):
    events = Event.objects.filter(
        is_published=True,
        start_date__gte=timezone.now()
    ).order_by('start_date')

    return render(request, "participants/home.html", {
        "events": events
    })

# LOGIN

def participant_login(request):
    if request.method == "POST":
        last_name = request.POST.get("last_name")
        year = request.POST.get("year")

        participant = Participant.objects.filter(
            last_name__iexact=last_name,
            birthday__year=year
        ).first()

        if participant:
            messages.success(request, "Participant found!")
            return render(request, "participants/dashboard.html", {
                "participant": participant
            })
        else:
            messages.error(request, "No matching participant found.")

    return render(request, "participants/login.html")
    
# DASHBOARD
@login_required
def dashboard(request):
    participant_id = request.session.get("participant_id")

    if not participant_id:
        return redirect("participants:login")

    try:
        participant = Participant.objects.get(id=participant_id)
    except Participant.DoesNotExist:
        logout(request)
        request.session.flush()
        messages.error(request, "Session expired. Please log in again.")
        return redirect("participants:login")

    return render(request, "participants/dashboard.html", {
        "participant": participant
    })


# LOGOUT
def participant_logout(request):
    logout(request)
    request.session.flush()
    return redirect("participants:home")


@login_required
def participants_dashboard(request):
    participant = request.user.participant
    return render(request, "participants/dashboard.html", { 
        "participant": participant
    })