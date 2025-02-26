"""
URL configuration for farm_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication.views import home


urlpatterns = [
    path('',home), # this link opens the login page
    path('admin/', admin.site.urls), # This URL pattern is used to access the admin site
    path('auth/', include('authentication.urls')), # This URL pattern is used to access the authentication app
    # path('milk/', include('milk.urls')), # This URL pattern is used to access the milk_management app
    path('animals/', include('animals.urls')), # This URL pattern is used to access the animal_management app
    path('immunization/', include('immunization.urls')), # This URL pattern is used to access the immunization app
    path('feeds/', include('feeds.urls')), # This URL pattern is used to access the feeds app
]
