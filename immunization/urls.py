from django.urls import path    
from . import views

urlpatterns = [
    path('add/', views.add_immunization, name='add_immunization'),
    path('list/', views.immunization_list, name='immunization_list'),
    path('edit/<int:immunization_id>/', views.edit_immunization, name='edit_immunization'),  # Add path for editing immunizations
    path('delete/<int:immunization_id>/', views.delete_immunization, name='delete_immunization'),  # Add path for deleting immunizations
    path('get_animal_tags_by_category/', views.get_animal_tags_by_category, name='get_animal_tags_by_category'),
]