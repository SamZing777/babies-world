from rest_framework import (
	generics,
	permissions,
	authentication,
	throttling
	)

from .models import HealthTipsForBaby
from .serializers import HealthTipSerializer

from products.permissions import (
	IsOwnerOrReadOnly
	)


class TipListAPIView(generics.ListCreateAPIView):
	queryset = HealthTipsForBaby.objects.all()
	serializer_class = HealthTipSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	throttle_scope = 'tips'
	throttle_classes = (throttling.ScopedRateThrottle,)


class TipDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = HealthTipsForBaby.objects.all()
	serializer_class = HealthTipSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
	authentication_classes = [authentication.TokenAuthentication]
	throttle_scope = 'tips'
	throttle_classes = (throttling.ScopedRateThrottle,)
