from django.urls import path
from .views import SubscriptionListAPIView

urlpatterns = [
    path('subscriptions/', SubscriptionListAPIView.as_view() )
]
