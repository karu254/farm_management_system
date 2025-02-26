from django import forms
from .models import Immunization, ImmunizationRecord
from animals.models import Animal

class ImmunizationTypeForm(forms.ModelForm):
    class Meta:
        model = Immunization
        fields = ['immunization_name', 'applicable_category', 'description', 'date_administered']

    applicable_category = forms.ChoiceField(choices=[('calf', 'Calf'), ('milking_cow', 'Milking Cow'), ('bull', 'Bull')])
    date_administered = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class ImmunizationRecordForm(forms.ModelForm):
    class Meta:
        model = ImmunizationRecord
        fields = ['animal', 'immunization_type', 'date_administered', 'immunized']

    animal = forms.ModelChoiceField(queryset=Animal.objects.all(), empty_label="Select Animal", widget=forms.Select(attrs={'class': 'form-control'}))
    immunized = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
