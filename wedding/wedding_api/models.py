from django.db import models
from users.models import User


class Wedding(models.Model):
    groom_name = models.CharField(max_length=100)
    bride_name = models.CharField(max_length=100)
    groom_info = models.TextField(null=True, blank=True)  # Info like age, origin, etc.
    bride_info = models.TextField(null=True, blank=True)  # Info like age, origin, etc.
    wedding_date = models.DateTimeField()
    vanue_name = models.CharField(max_length=255) #The specific name of the venue where the wedding is held.
    location = models.CharField(max_length=255)  # Integrated with Yandex Maps
    latitude = models.FloatField()
    longitude = models.FloatField()
    invitation_style = models.CharField(max_length=255, null=True, blank=True)
    qr_code_style = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weddings')
    donation_card_number = models.CharField(max_length=20, blank=True, null=True)


