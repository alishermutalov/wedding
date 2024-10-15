from datetime import timezone
from django.db import models
from users.models import User, BASIC, STANDARD, PREMIUM
from wedding_api.models import Wedding

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
    features = models.JSONField(null=True, blank=True)  # Store plan features as JSON

    def __str__(self):
        return self.tariff_plan
    

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscription")
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE, related_name="subscriptions")  # Each subscription is tied to a wedding
    tariff_plan = models.ForeignKey(TariffPlan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.end_date and self.wedding:
            self.end_date = self.wedding.wedding_date
        super().save(*args, **kwargs)
    
    def update_status(self):
        if timezone.now() > self.end_date:
            self.is_active = False
            self.save()



