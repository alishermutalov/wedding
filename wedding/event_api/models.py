from django.db import models
from wedding_api.models import Wedding

# Create your models here.
class Event(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    background_image = models.ImageField(upload_to="event_images/")
