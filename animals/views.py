from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import MilkRecord, Animal
from .models import Animal
from .forms import AnimalForm, MilkRecordForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q # Import Q for search queries

def animal_list(request):
    animals = Animal.objects.all()

    # Search by tag number
    search_query = request.GET.get('search', '')
    if search_query:
        animals = animals.filter(tag_number__icontains=search_query)

    # Filters
    category = request.GET.get('category')
    gender = request.GET.get('gender')
    health_status = request.GET.get('health_status')

    if category:
        animals = animals.filter(category=category)
    if gender:
        animals = animals.filter(gender=gender)
    if health_status:
        animals = animals.filter(health_status=health_status)

    # Pagination (10 animals per page)
    paginator = Paginator(animals, 10) # Show 10 animals per page
    try:    # Get the page number from the request
        page_number = int(request.GET.get('page', 1)) # Default to page 1
    except:
        page_number = 1 # Default to page 1
    page_obj = paginator.get_page(page_number) # Get the animals for the requested page

    context = {
        'animals': page_obj,  # Paginated animals
        'search_query': search_query,
        'category': category,
        'gender': gender,
        'health_status': health_status,
    }
    return render(request, 'animals/animal_list.html', context)

# def add_animal(request):
#     """Handle adding a new animal."""
#     if request.method == "POST":
#         form = AnimalForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Animal added successfully!")
#             return redirect('animal_list')
#     else:
#         form = AnimalForm()
#     return render(request, 'animals/add_animal.html', {'form': form})



def add_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)  # Get instance but don’t save yet
            animal.save()  # Calls save() to auto-assign category
            messages.success(request, "Animal added successfully!")
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'animals/add_animal.html', {'form': form})





def edit_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal details updated successfully!")
            return redirect('animal_list')
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'animals/edit_animal.html', {'form': form, 'animal': animal})



def delete_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        animal.delete()
        messages.success(request, "Animal deleted successfully!")
        return redirect('animal_list')

    return render(request, 'animals/delete_animal.html', {'animal': animal})










# milk record

def milk_record_list(request):
    records = MilkRecord.objects.all().order_by('-date')

    # Filtering by date range
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date and end_date:
        records = records.filter(date__range=[start_date, end_date])

    # Searching by cow's tag number
    search_query = request.GET.get('search')
    if search_query:
        records = records.filter(cow__tag_number__icontains=search_query)

    # Pagination (show 10 records per page)
    paginator = Paginator(records, 10)
    page_number = request.GET.get('page')
    milk_records = paginator.get_page(page_number)

    return render(request, 'milk/milk_record_list.html', {
        'milk_records': milk_records,
        'start_date': start_date,
        'end_date': end_date,
        'search_query': search_query
    })
def add_milk_record(request):
    if request.method == 'POST':
        form = MilkRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('milk_record_list')
    else:
        form = MilkRecordForm()
    
    return render(request, 'milk/add_milk_record.html', {'form': form})

def edit_milk_record(request, record_id):
    record = get_object_or_404(MilkRecord, id=record_id)
    if request.method == 'POST':
        form = MilkRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('milk_record_list')
    else:
        form = MilkRecordForm(instance=record)
    
    return render(request, 'milk/edit_milk_record.html', {'form': form})

def delete_milk_record(request, record_id):
    record = get_object_or_404(MilkRecord, id=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('milk_record_list')

    return render(request, 'milk/delete_milk_record.html', {'record': record})

