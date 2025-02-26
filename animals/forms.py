from django import forms
from .models import Animal, MilkRecord

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['tag_number', 'name', 'birth_date', 'gender', 'health_status']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }


class MilkRecordForm(forms.ModelForm):
    class Meta:
        model = MilkRecord
        fields = ['cow', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter milk quantity'}),
        }