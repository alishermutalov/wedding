from .models import Subscription, TariffPlan
from  rest_framework import serializers


class TariffPlanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TariffPlan
        fields = ['name', 'description', 'tariff_plan', 'price', 'features']
        
        