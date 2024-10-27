from .models import Wedding
from rest_framework import serializers


class WeddingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, required=False)
    