from django.urls import path
from .views import pending_immunizations

urlpatterns = [
    path("pending/", pending_immunizations, name="pending_immunizations"),
]
