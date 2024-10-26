from django.db import models
from rest_framework.exceptions import ValidationError
from wedding_api.models import Wedding
from users.utils import check_phone_number
from django.urls import reverse

class Guest(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="guests")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)
    qr_code = models.ImageField(upload_to="wedding/invations/qr/", null=True, blank=True )
    is_attending = models.BooleanField(default=False)
    invite_link = models.URLField(blank=True, null=True)
    total_donations = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True, null=True)

    def save(self, *args, **kwargs):
        if check_phone_number(self.phone_number):
            # Only generate invite link if not already set
            if not self.invite_link:
                # Pass the request object when calling from a view
                domain = "127.0.0.1:8000" #kwargs.pop('domain', None)
                path = self.phone_number #reverse('invitation_view', args=[self.phone_number])
                self.invite_link = f"https://{domain}/invation/{path}"
            super().save(*args, **kwargs)
        else:
            raise ValidationError("Invalid phone number format.")