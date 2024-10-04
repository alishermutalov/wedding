from django.db import models
from wedding_api.models import Wedding
from guest.models import Guest


class Comment(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="comments")
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
