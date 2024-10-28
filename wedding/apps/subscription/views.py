from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import SubscriptionSerializer
from .models import Subscription

class SubscriptionListAPIView(ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)