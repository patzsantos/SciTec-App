"""Converts the ISS environment and range database"""

from rest_framework import serializers
from .models import Range, Environment


class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Range
        fields = '__all__'


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'
