from django.db import models
from datetime import date

class Animal(models.Model):
    ANIMAL_TYPES = [
        ('calf', 'Calf'),
        ('milking_cow', 'Milking Cow'),
        ('bull', 'Bull'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    tag_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    category = models.CharField(max_length=20, choices=ANIMAL_TYPES, blank=True)
    health_status = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """ Automatically assign category based on age and gender """
        age_in_days = (date.today() - self.birth_date).days
        age_in_years = age_in_days / 365  # Convert days to years

        if age_in_years < 1:
            self.category = 'calf'
        elif self.gender == 'male':
            self.category = 'bull'
        elif self.gender == 'female' and age_in_years >= 2:  # Female cows older than 2 years are milking cows
            self.category = 'milking_cow'
        else:
            self.category = 'calf' # Default to calf if no condition is met

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.category} ({self.tag_number})"


class MilkRecord(models.Model):
    cow = models.ForeignKey(Animal, on_delete=models.CASCADE, limit_choices_to={'category': 'milking_cow'})
    date = models.DateField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2, help_text="Liters of milk produced")

    def __str__(self):
        return f"{self.cow.name} - {self.date}: {self.quantity}L"
