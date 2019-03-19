from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6)
    class Meta:
        model = Customer
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')

