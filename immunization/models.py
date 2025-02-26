from django.db import models
from animals.models import Animal

class Immunization(models.Model):
    immunization_name = models.CharField(max_length=100)
    applicable_category = models.CharField(max_length=20, choices=[('calf', 'Calf'), ('milking_cow', 'Milking Cow'), ('bull', 'Bull')])
    description = models.TextField(blank=True, null=True)
    date_administered = models.DateField()

    def __str__(self):
        return f"{self.immunization_name} for {self.applicable_category}"

class ImmunizationRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    immunization_type = models.ForeignKey(Immunization, on_delete=models.CASCADE)
    date_administered = models.DateField()
    immunized = models.BooleanField(default=False)

    def __str__(self):
        return f"Immunization for {self.animal.tag_number} ({self.immunization_type.immunization_name})"
