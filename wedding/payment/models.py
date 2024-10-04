from django.db import models
from users.models import User, BASIC, STANDARD, PREMIUM


class Payment(models.Model):
    TARIFF_PLANS = (
        (BASIC,BASIC),
        (STANDARD,STANDARD),
        (PREMIUM,PREMIUM),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    tariff_plan = models.CharField(max_length=20, choices=TARIFF_PLANS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    transaction_id = models.CharField(max_length=100)
