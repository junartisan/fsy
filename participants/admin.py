from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'stake_district_mission',
        'application_type',
        'group',
        'room',
    )

    list_filter = (
        'stake_district_mission',
        'group',
        'room',
        'application_type',
        'gender',
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
        'group',
        'room',
    )
