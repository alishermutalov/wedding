from django.db import models
from wedding_api.models import Wedding

# Create your models here.
class Gallery(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="galleries")
    image = models.ImageField(upload_to="wedding_gallery/")
    description = models.CharField(max_length=255)
