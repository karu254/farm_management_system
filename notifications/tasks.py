from django.core.mail import send_mail
from django.contrib.auth.models import User
from animals.models import AnimalImmunization

def send_weekly_notifications():
    pending_animals = AnimalImmunization.objects.filter(is_immunized=False)
    users = User.objects.filter(notification_pref__email_notifications=True)

    for user in users:
        pending_list = "\n".join([f"{a.animal.tag_number} - {a.immunization.immunization_name}" for a in pending_animals])
        message = f"Dear {user.username},\n\nThe following animals need immunization:\n\n{pending_list}\n\nPlease take action."
        
        send_mail(
            "Pending Immunizations Alert",
            message,
            "henrykaru77@gmail.com",
            [user.email],
            fail_silently=False,
        )
