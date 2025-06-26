from rest_framework import serializers, generics
from .models import Terminal

class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ['name', 'description', 'price', 'in_stock']

class TerminalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ['id', 'name', 'description', 'price', 'in_stock']