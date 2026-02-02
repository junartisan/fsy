from django.db import models

class Participant(models.Model):
    STAKE_CHOICES = [
        ("cebu_city_stake", "Cebu City Stake"),
        ("cebu_central_stake", "Cebu Central Stake"),
        ("bogo_district", "Bogo District"),
    ]
    timestamp = models.DateTimeField(null=True, blank=True)

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    preferred_name = models.CharField(max_length=100, blank=True)

    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=22)
    application_type = models.CharField(max_length=100)

    phone = models.CharField(max_length=30)

    guardian_name = models.CharField(max_length=150, blank=True)
    guardian_email = models.EmailField(blank=True)
    guardian_phone = models.CharField(max_length=30, blank=True)

    emergency_contact_name = models.CharField(max_length=150, blank=True)
    emergency_contact_email = models.EmailField(blank=True)
    emergency_contact_phone = models.CharField(max_length=30, blank=True)

    stake_district_mission = models.CharField(
        max_length=50, 
        choices=STAKE_CHOICES
    )
    ward_branch = models.CharField(max_length=200)
    bishop = models.CharField(max_length=150, blank=True)

    medical_info = models.TextField(blank=True)
    dietary_info = models.TextField(blank=True)

    requires_attention = models.CharField(max_length=250, blank=True)

    tshirt_size = models.CharField(max_length=10, blank=True)
    agreed_terms_text = models.TextField(blank=True)

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
        return f"{self.first_name} {self.last_name}"
