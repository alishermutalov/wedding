from .models import Subscription, TariffPlan
from  rest_framework import serializers
from apps.wedding_api.serializers import WeddingSerializer

class TariffPlanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TariffPlan
        fields = ['name', 'description', 'tariff_plan', 'price', 'features']
        

class SubscriptionSerializer(serializers.ModelSerializer):
    tariff_plan = TariffPlanSerializer(read_only=True)
    wedding = WeddingSerializer(read_only=True)
    
   