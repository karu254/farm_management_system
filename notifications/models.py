# from django.db import models
# from django.contrib.auth.models import User  # Assuming farmers use Django's User model

# class NotificationPreference(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="notification_pref")
#     email_notifications = models.BooleanField(default=True)  # Farmers can opt in/out

#     def __str__(self):
#         return f"{self.user.username} - Notifications: {'On' if self.email_notifications else 'Off'}"




from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class NotificationPreference(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notification_pref")
    email_notifications = models.BooleanField(default=True)  # Farmers can opt in/out

    def __str__(self):
        return f"{self.user.username} - Notifications: {'On' if self.email_notifications else 'Off'}"
