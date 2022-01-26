from rest_framework import serializers

from .models import HealthTipsForBaby


class HealthTipSerializer(serializers.ModelSerializer):

	class Meta:
		model = HealthTipsForBaby
		fields = '__all__'
