from rest_framework import serializers

from .models import VPS


class VPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPS
        fields = ['uid', 'cpu', 'ram', 'hdd', 'status']
