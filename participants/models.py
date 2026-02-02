from django.db import models

class Participant(models.Model):
    STAKE_CHOICES = [
        ("cebu_city_stake", "Cebu City Stake"),
        ("cebu_central_stake", "Cebu Central Stake"),
        ("bogo_district", "Bogo District"),
    ]

    APPLICATION_CHOICES = [
        ("participant", "Participant"),
        ("counselor", "Counselor"),
        ("assistant_coordinator", "Assistant Coordinator"),
        ("coordinator", "Coordinator"),
    ]

    # Time tracking
    timestamp = models.DateTimeField(auto_now_add=True, null=True) # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True) # Automatically set on every save (edit)

    # Personal Info
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    preferred_name = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=22)
    
    # Updated to use choices
    application_type = models.CharField(
        max_length=100, 
        choices=APPLICATION_CHOICES,
        default="participant"
    )

    phone = models.CharField(max_length=30)

    # Guardian / Emergency
    guardian_name = models.CharField(max_length=150, blank=True)
    guardian_email = models.EmailField(blank=True)
    guardian_phone = models.CharField(max_length=30, blank=True)

    emergency_contact_name = models.CharField(max_length=150, blank=True)
    emergency_contact_email = models.EmailField(blank=True)
    emergency_contact_phone = models.CharField(max_length=30, blank=True)

    # Church Info
    stake_district_mission = models.CharField(
        max_length=50, 
        choices=STAKE_CHOICES
    )
    ward_branch = models.CharField(max_length=200)
    bishop = models.CharField(max_length=150, blank=True)

    # Medical & Preferences
    medical_info = models.TextField(blank=True)
    dietary_info = models.TextField(blank=True)
    requires_attention = models.CharField(max_length=250, blank=True)
    tshirt_size = models.CharField(max_length=10, blank=True)

    # --- NEW: Terms & Conditions Persistence ---
    agree_to_terms = models.BooleanField(default=False) 
    agreed_terms_text = models.TextField(blank=True)

    # Admin Assignments
    group = models.CharField(
        max_length=50,
        blank=True,
        help_text="FSY group assignment (e.g. Group A, Group 1)"
    )
    room = models.CharField(
        max_length=50,
        blank=True,
        help_text="Room assignment (e.g. Room 101)"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_application_type_display()})"