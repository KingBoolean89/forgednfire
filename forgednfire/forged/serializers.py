from rest_framework import serializers
from .models import Forged

class ForgedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forged
        fields('name', 'length', 'blade', 'steelgrade', 'createdAt')