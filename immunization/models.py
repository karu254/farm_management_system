from django.db import models
from animals.models import Animal

class Immunization(models.Model):
    VACCINE_CATEGORIES = [
        ('calf', 'Calf'),
        ('milking_cow', 'Milking Cow'),
        ('bull', 'Bull'),
    ]
    immunization_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=VACCINE_CATEGORIES)
    quantity = models.DecimalField(default=0, max_digits=5, decimal_places=2, help_text="Quantity of vaccine per animal per day (ml or mg)")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.immunization_name