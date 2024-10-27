from datetime import date

from rest_framework import serializers

from .models import Wedding


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
        
    def validate_groom_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Groom's name must contain only letters.")
        return value

    def validate_bride_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Bride's name must contain only letters.")
        return value

    def validate_wedding_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Wedding date must be in the future.")
        return value

    def validate_donation_card_number(self, value):
        if not value.isdigit() or len(value) != 16:
            raise serializers.ValidationError("Donation card number must be a 16-digit number.")
        return value

    def validate(self, data):
        if data.get('latitude') is None or data.get('longitude') is None:
            raise serializers.ValidationError("Both latitude and longitude are required for the wedding location.")
        
        if not (-90 <= data['latitude'] <= 90) or not (-180 <= data['longitude'] <= 180):
            raise serializers.ValidationError("Latitude must be between -90 and 90 and longitude between -180 and 180.")
        
        return data
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().update(instance, validated_data)
    
    