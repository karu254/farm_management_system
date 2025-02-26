from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from django.db.models import Sum
from animals.models import Animal, MilkRecord # Import Animal and MilkRecord models
from django.db.models.functions import TruncDate
import json
from datetime import date, datetime


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! You are now logged in.")
            return redirect('dashboard')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Both fields are required.")
            return render(request, "authentication/login.html", {"form": LoginForm()})

        user = authenticate(request, username=username, password=password)

        print("DEBUG: User object returned from authenticate ->", user)  # Debugging line

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("dashboard")
            else:
                messages.error(request, "Account is inactive. Contact admin.")
        else:
            messages.error(request, "Invalid username or password.")
            print("DEBUG: Authentication failed for username:", username)  # Debugging line

    return render(request, "authentication/login.html", {"form": LoginForm()})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')



# @login_required
def dashboard_view(request):
    total_animals = Animal.objects.count()
    calves = Animal.objects.filter(category="calf").count()
    milking_cows = Animal.objects.filter(category="milking_cow").count()
    bulls = Animal.objects.filter(category="bull").count()
    # Milk Production (Past Week)
    today = date.today()
    week_days = [(today - timedelta(days=i)).strftime('%A') for i in range(6, -1, -1)]  # Get last 7 days

    milk_data = [
        float(MilkRecord.objects.filter(date=today - timedelta(days=i)).aggregate(Sum('quantity'))['quantity__sum'] or 0)
        for i in range(6, -1, -1)
    ]

    # milk_data = []
    
    # for i in range(6, -1, -1):
    #     day = today - timedelta(days=i)
    #     total_milk = MilkRecord.objects.filter(date=day).aggregate(Sum('quantity'))['quantity__sum'] or 0
    #     milk_data.append(total_milk)



    # Milk Production (Today)
    daily_milk = MilkRecord.objects.filter(date=date.today()).aggregate(Sum('quantity'))['quantity__sum'] or 0
    daily_milk = float(daily_milk)


    context = {
        'total_animals': total_animals,
        'calves': calves,
        'milking_cows': milking_cows,
        'bulls': bulls,
        'week_days': json.dumps(week_days),
        'milk_data': json.dumps(milk_data),
        'daily_milk': daily_milk,
    }
    return render(request, 'authentication/dashboard.html', context)




def home(request):
    return render(request, 'authentication/dashboard.html') # Change this to 'authentication/dashboard.html' later
