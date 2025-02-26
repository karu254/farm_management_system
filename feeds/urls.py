# feeds/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_feed, name='add_feed'),
    path('list/', views.feed_list, name='feed_list'),
    path('edit/<int:feed_id>/', views.edit_feed, name='edit_feed'),  # Add path for editing feeds
    path('delete/<int:feed_id>/', views.delete_feed, name='delete_feed'),  # Add path for deleting feeds
    path('get_animal_tags_by_category/', views.get_animal_tags_by_category, name='get_animal_tags_by_category'),
]
