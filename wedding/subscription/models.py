from datetime import timezone
from django.db import models
from users.models import User, BASIC, STANDARD, PREMIUM


class Subscription(models.Model):
    TARIFF_PLANS = (
        (BASIC,BASIC),
        (STANDARD,STANDARD),
        (PREMIUM,PREMIUM),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="subscription")
    tariff_plan = models.CharField(max_length=20, choices=TARIFF_PLANS)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    
    def update_status(self):
        if timezone.now() > self.end_date:
            self.is_active = False
            self.save()
