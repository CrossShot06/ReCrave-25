from django import forms
from .models import StallRegistration # <-- Change this

class StallRegistrationForm(forms.ModelForm): # <-- Renamed
    class Meta:
        model = StallRegistration # <-- Change this
        # Update the fields list
        fields = ['stall_name', 'contact_person', 'email', 'phone', 'cuisine_type', 'stall_requirements']