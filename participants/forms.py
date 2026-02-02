from django import forms
from .models import Participant

class ParticipantLoginForm(forms.Form):
    """
    Login using Last Name and Birth Year.
    """
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={"class": "w-full p-3 border rounded", "placeholder": "Enter Last Name"})
    )
    year = forms.IntegerField(
        label="Birth Year",
        widget=forms.NumberInput(attrs={"class": "w-full p-3 border rounded", "placeholder": "YYYY"})
    )


class ParticipantRegistrationForm(forms.ModelForm):
    # Add the terms checkbox manually since it's not in the model
    agree_to_terms = forms.BooleanField(
        label="I agree to the Terms and Conditions",
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'h-5 w-5 text-blue-600 border-gray-300 rounded focus:ring-blue-500 cursor-pointer'
        })
    )

    class Meta:
        model = Participant
        fields = [
            "email", "first_name", "last_name", "preferred_name",
            "birthday", "gender", "application_type", "phone",
            "guardian_name", "guardian_email", "guardian_phone",
            "emergency_contact_name", "emergency_contact_email", "emergency_contact_phone",
            "stake_district_mission", "ward_branch", "bishop",
            "medical_info", "dietary_info", "tshirt_size",
            "agreed_terms_text",
        ]

        widgets = {
            "birthday": forms.DateInput(attrs={
                "type": "date",
                "class": "w-full border rounded-lg p-2"
            }),
            "medical_info": forms.Textarea(attrs={
                "rows": 3, "placeholder": "Allergies, conditions, etc.",
                "class": "w-full border rounded-lg p-2"
            }),
            "dietary_info": forms.Textarea(attrs={
                "rows": 3, "placeholder": "Vegetarian, No pork, etc.",
                "class": "w-full border rounded-lg p-2"
            }),
            "agreed_terms_text": forms.Textarea(attrs={
                "rows": 3, "readonly": True,
                "class": "bg-gray-50 text-gray-500 text-sm w-full border rounded-lg p-2"
            }),
            "application_type": forms.Select(attrs={"class": "w-full border rounded-lg p-2"}),
            "stake_district_mission": forms.Select(attrs={"class": "w-full border rounded-lg p-2"}),
            "gender": forms.Select(choices=[('Male','Male'),('Female','Female')], attrs={"class":"w-full border rounded-lg p-2"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set default text for Terms box
        self.fields['agreed_terms_text'].initial = (
            "I hereby agree to follow the FSY standards and code of conduct. "
            "I understand that my participation is subject to the rules of the event."
        )

        # Make email read-only if editing
        if self.instance and self.instance.pk:
            self.fields['email'].widget.attrs.update({
                'readonly': True,
                'class': 'bg-gray-100 cursor-not-allowed w-full border rounded-lg p-2'
            })
            # Make agree_to_terms True for existing instances
            self.initial['agree_to_terms'] = True
