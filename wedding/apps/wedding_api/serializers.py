from .models import Wedding
from rest_framework import serializers


class WeddingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, required=False)
    
    class Meta:
        model = Wedding
        fields = [
            'user',
            'groom_name',
            'bride_name',
            'groom_info',
            'bride_info',
            'wedding_date',
            'vanue_name',
            'location',
            'latitude',
            'longitude',
            'invitation_style',
            'qr_code_style',
            'donation_card_number',
        ]