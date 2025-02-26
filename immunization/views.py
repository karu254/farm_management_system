from django.shortcuts import render, redirect
from .models import Immunization, ImmunizationRecord
from .forms import ImmunizationTypeForm, ImmunizationRecordForm
from django.contrib import messages
from django.utils import timezone
from animals.models import Animal
from django.db.models import F
from datetime import timedelta









def add_immunization(request):
    if request.method == 'POST':
        # Process Immunization Type Form
        immunization_form = ImmunizationTypeForm(request.POST)
        immunization_record_form = ImmunizationRecordForm(request.POST)

        if immunization_form.is_valid():
            immunization_form.save()
            messages.success(request, "Immunization Type added successfully!")

        # Process Immunization Record Form
        if immunization_record_form.is_valid():
            immunization_record_form.save()
            messages.success(request, "Immunization Record added successfully!")

        return redirect('immunization_schedule')
    else:
        immunization_form = ImmunizationTypeForm()
        immunization_record_form = ImmunizationRecordForm()

    return render(request, 'immunization/add_immunization.html', {
        'immunization_form': immunization_form,
        'immunization_record_form': immunization_record_form
    })

def immunization_schedule(request):
    # Filter records for this week based on birthdate and category
    today = timezone.now()
    animals_due_for_immunization = Animal.objects.all()

    records = ImmunizationRecord.objects.filter(immunized=False).filter(date_administered__gte=today - timedelta(days=7))

    context = {
        'animals_due_for_immunization': animals_due_for_immunization,
        'immunization_records': records
    }
    return render(request, 'immunization/immunization_schedule.html', context)

def immunization_records(request):
    records = ImmunizationRecord.objects.all()

    context = {
        'immunization_records': records
    }
    return render(request, 'immunization/immunization_records.html', context)



# @login_required
def immunization_records(request):
    # Fetch all immunization records
    immunization_records = ImmunizationRecord.objects.all()
    
    context = {
        'immunization_records': immunization_records
    }
    return render(request, 'immunization/immunization_records.html', context)