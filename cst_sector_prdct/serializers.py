# serializers.py in your app directory

from rest_framework import serializers
from .models import Sector, Industry, VerticalMarket, Application, Algorithm   # new


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id', 'name', 'description', 'created_at']

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'name', 'sector', 'description', 'created_at']

class VerticalMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerticalMarket
        fields = ['id', 'name', 'industry', 'description', 'created_at']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name', 'vertical_market', 'description', 'created_at']

class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algorithm
        fields = ['id', 'name', 'application', 'description', 'created_at']
        