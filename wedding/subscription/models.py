from datetime import timezone
from django.db import models
from users.models import User, BASIC, STANDARD, PREMIUM


class TariffPlan(models.Model):
    TARIFF_PLANS = (
        (BASIC,BASIC),
        (STANDARD,STANDARD),
        (PREMIUM,PREMIUM),
    )
    name = models.CharField(max_length=50)
    tariff_plan = models.CharField(max_length=50, choices=TARIFF_PLANS)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_in_days = models.IntegerField(default=30)  # Duration of the plan, e.g., 30 days
    features = models.JSONField(null=True, blank=True)  # Store plan features as JSON

    def __str__(self):
        return self.tariff_plan
    

class Subscription(models.Model):
    TARIFF_PLANS = (
        (BASIC,BASIC),
        (STANDARD,STANDARD),
        (PREMIUM,PREMIUM),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="subscription")
    tariff_plan = models.ForeignKey(TariffPlan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    def update_status(self):
        if timezone.now() > self.end_date:
            self.is_active = False
            self.save()



