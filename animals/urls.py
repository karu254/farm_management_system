

from django.urls import path
from .views import animal_list, add_animal, edit_animal, delete_animal, milk_record_list, add_milk_record, edit_milk_record, delete_milk_record

urlpatterns = [
    path('list/', animal_list, name='animal_list'),
    path('add/', add_animal, name='add_animal'),

    path('edit/<int:animal_id>/', edit_animal, name='edit_animal'),
    path('delete/<int:animal_id>/', delete_animal, name='delete_animal'),
    path('milk/list/', milk_record_list, name='milk_record_list'),
    path('milk/add/', add_milk_record, name='add_milk_record'),
    path('milk/edit/<int:record_id>/', edit_milk_record, name='edit_milk_record'),
    path('milk/delete/<int:record_id>/', delete_milk_record, name='delete_milk_record'),
]



