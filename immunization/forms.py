from django import forms
from .models import Immunization
from animals.models import Animal # Import the Animal model to reference categories

class ImmunizationForm(forms.ModelForm):
    class Meta:
        model = Immunization
        fields = ['immunization_name', 'category', 'quantity', 'description']
        widgets = {
            'category': forms.Select(choices=Immunization.VACCINE_CATEGORIES),
        }