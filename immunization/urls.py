from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_immunization, name='add_immunization'),
    path('schedule/', views.immunization_schedule, name='immunization_schedule'),
    path('records/', views.immunization_records, name='immunization_records'),
    path('immunization-records/', views.immunization_records, name='immunization_records'),

]
