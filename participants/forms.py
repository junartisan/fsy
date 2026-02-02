from django import forms
from .models import Participant

class ParticipantLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "w-full p-3 border rounded",
            "placeholder": "Enter your registered email"
        })
    )

class ParticipantRegistrationForm(forms.ModelForm):
    # Defining specific roles for application_type
    APPLICATION_CHOICES = [
        ("participant", "Participant"),
        ("counselor", "Counselor"),
        ("assistant_coordinator", "Assistant Coordinator"),
        ("coordinator", "Coordinator"),
    ]

    application_type = forms.ChoiceField(
        choices=APPLICATION_CHOICES,
        label="Application Type",
        widget=forms.Select(attrs={"class": "w-full border rounded-lg p-2"})
    )

    # This field handles the "must check" validation in the UI
    agree_to_terms = forms.BooleanField(
        required=True,
        label="I agree to the Terms and Conditions",
        error_messages={'required': 'You must agree to the terms to proceed.'}
    )

    class Meta:
        model = Participant
        fields = [
            "email",
            "first_name",
            "last_name",
            "preferred_name",
            "birthday",
            "gender",
            "application_type",
            "phone",
            "guardian_name",
            "guardian_email",
            "guardian_phone",
            "emergency_contact_name",
            "emergency_contact_email",
            "emergency_contact_phone",
            "stake_district_mission",
            "ward_branch",
            "bishop",
            "medical_info",
            "dietary_info",
            "tshirt_size",
            "agreed_terms_text", # Kept for your model records
        ]

        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
            "medical_info": forms.Textarea(attrs={"rows": 3, "placeholder": "Allergies, conditions, etc."}),
            "dietary_info": forms.Textarea(attrs={"rows": 3, "placeholder": "Vegetarian, No pork, etc."}),
            "agreed_terms_text": forms.Textarea(attrs={
                "rows": 3, 
                "readonly": "readonly",
                "class": "bg-gray-50 text-gray-500 text-sm"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Set a default value for the terms text if you want it visible
        self.fields['agreed_terms_text'].initial = "I hereby agree to follow the FSY standards and code of conduct..."