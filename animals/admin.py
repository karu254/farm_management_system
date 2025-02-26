from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('tag_number', 'name', 'category', 'birth_date', 'gender', 'health_status')
    search_fields = ('tag_number', 'name')
    list_filter = ('category', 'gender')
