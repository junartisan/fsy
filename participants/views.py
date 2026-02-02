from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import ParticipantRegistrationForm, ParticipantLoginForm
from .models import Participant

# 1. ADDED THIS: The missing 'home' view
def home(request):
    # If you have an Event model, you can filter it here
    # For now, we'll just render the home page
    return render(request, "participants/home.html")

# REGISTRATION
def participant_register(request):
    # --- ADD THIS BLOCK ---
    # If the user is already logged in, send them to the dashboard
    if request.session.get("participant_id"):
        return redirect("participants:dashboard")
    # ----------

    if request.method == "POST":
        form = ParticipantRegistrationForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.timestamp = timezone.now()
            participant.save()

            messages.success(request, f"Registration successful for {participant.first_name}!")
            # Use the namespace 'participants:login'
            return redirect("participants:login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ParticipantRegistrationForm()

    return render(request, "participants/register.html", {
        "form": form
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
            # Set the session
            request.session["participant_id"] = participant.id
            messages.success(request, f"Welcome back, {participant.first_name}!")
            return redirect("participants:dashboard")
        else:
            messages.error(request, "No matching participant found. Check your Last Name and Birth Year.")

    return render(request, "participants/login.html")

# DASHBOARD
def dashboard(request):
    participant_id = request.session.get("participant_id")

    if not participant_id:
        messages.error(request, "Please login to access your dashboard.")
        return redirect("participants:login")

    try:
        participant = Participant.objects.get(id=participant_id)
    except Participant.DoesNotExist:
        return redirect("participants:login")

    return render(request, "participants/dashboard.html", {
        "participant": participant
    })

# LOGOUT
def participant_logout(request):
    # This removes all data from the session and deletes the session cookie
    request.session.flush()
    
    # Add a friendly message
    messages.info(request, "You have been successfully logged out.")
    
    # Send them back to the home page
    return redirect("participants:home")