from django.shortcuts import render
from animals.models import AnimalImmunization

def pending_immunizations(request):
    pending_animals = AnimalImmunization.objects.filter(is_immunized=False)
    return render(request, "notifications/pending_immunizations.html", {"pending_animals": pending_animals})
