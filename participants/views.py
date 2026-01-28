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
    form = ParticipantLoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"].lower()

        try:
            participant = Participant.objects.get(email__iexact=email)
        except Participant.DoesNotExist:
            messages.error(
                request,
                "❌ Email not found. Please use the email you registered for FSY."
            )
            return render(request, "participants/login.html", {"form": form})

        # Create or update Django user
        user, created = User.objects.get_or_create(
            username=email,
            defaults={"email": email}
        )

        if not user.email:
            user.email = email
            user.save()

        login(request, user)

        request.session["participant_id"] = participant.id

        return redirect("participants:dashboard")

    return render(request, "participants/login.html", {"form": form})


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