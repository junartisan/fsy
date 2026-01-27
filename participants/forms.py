from django import forms

class ParticipantLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "w-full p-3 border rounded",
            "placeholder": "Enter your registered email"
        })
    )
