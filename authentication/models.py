from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any custom fields if necessary
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Prevents clash with auth.User.groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Prevents clash with auth.User.user_permissions
        blank=True
    )
