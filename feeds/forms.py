# feeds/forms.py
from django import forms
from .models import Feed
from animals.models import Animal  # Import the Animal model to reference categories

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['feed_name', 'category', 'quantity_per_animal', 'description']
        widgets = {
            'category': forms.Select(choices=Feed.FEED_CATEGORIES),
        }
