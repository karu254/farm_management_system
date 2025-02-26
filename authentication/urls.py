from django.urls import path # This is used to define URL patterns
from .views import register_view, login_view, logout_view, dashboard_view # This imports the views from the views.py file

urlpatterns = [
    path('register/', register_view, name='register'), # This URL pattern is used to register a new user
    path('login/', login_view, name='login'), # This URL pattern is used to log in an existing user
    path('logout/', logout_view, name='logout'), # This URL pattern is used to log out the user
    path('dashboard/', dashboard_view, name='dashboard'), # This URL pattern is used to display the dashboard
]
