from django.db import models
from rest_framework.exceptions import ValidationError
from wedding_api.models import Wedding
from users.utils import check_phone_number


class Guest(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="guests")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    qr_code = models.CharField(max_length=255)
    is_attending = models.BooleanField(default=False)
    total_donations = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True, null=True)

    def save(self, *args, **kwargs):
        if check_phone_number(self.phone_number):
            super().save(*args, **kwargs)
        else:
            raise ValidationError("Invalid phone number format.")