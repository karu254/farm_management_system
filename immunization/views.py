from django.shortcuts import render, redirect, get_object_or_404
from .models import Immunization
from .forms import ImmunizationForm
from django.http import JsonResponse
from animals.models import Animal
from django.contrib import messages

def add_immunization(request):
    if request.method == "POST":
        form = ImmunizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('immunization_list')  # After saving, redirect to immunization list page
    else:
        form = ImmunizationForm()

    return render(request, 'immunization/add_immunization.html', {'form': form})

def immunization_list(request):
    immunizations = Immunization.objects.all()

    context = {
        'immunizations': immunizations
    }
    return render(request, 'immunization/immunization_list.html', context)

def get_animal_tags_by_category(request):
    category = request.GET.get('category')
    animals = Animal.objects.filter(category=category)
    tag_numbers = [animal.tag_number for animal in animals]

    return JsonResponse(tag_numbers, safe=False)

def edit_immunization(request, immunization_id):
    immunization = get_object_or_404(Immunization, id=immunization_id)  # Fetch the immunization by its ID
    if request.method == "POST":
        form = ImmunizationForm(request.POST, instance=immunization)
        if form.is_valid():
            form.save()
            messages.success(request, "Immunization updated successfully!")
            return redirect('immunization_list')  # Redirect to the immunization list page after updating
    else:
        form = ImmunizationForm(instance=immunization)  # Populate the form with existing data

    return render(request, 'immunization/edit_immunization.html', {'form': form, 'immunization': immunization})

def delete_immunization(request, immunization_id):
    immunization = get_object_or_404(Immunization, id=immunization_id)  # Fetch the immunization by ID
    immunization.delete()
    messages.success(request, "Immunization deleted successfully!")
    return redirect('immunization_list')  # Redirect back to immunization list page after deletion