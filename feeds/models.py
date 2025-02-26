# feeds/models.py
from django.db import models
from animals.models import Animal  # Import Animal model for category reference

class Feed(models.Model):
    FEED_CATEGORIES = [
        ('calf', 'Calf'),
        ('milking_cow', 'Milking Cow'),
        ('bull', 'Bull'),
    ]

    feed_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=FEED_CATEGORIES)
    quantity_per_animal = models.DecimalField(max_digits=5, decimal_places=2, help_text="Quantity of feed per animal per day (kg or liters)")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.feed_name
