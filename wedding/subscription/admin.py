from django.contrib import admin
from .models import Subscription, TariffPlan


admin.site.register(Subscription)
admin.site.register(TariffPlan)