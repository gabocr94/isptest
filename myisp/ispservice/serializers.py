from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Customer, Plan, Contract


class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = Customer
        exclude=('user',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')

class Customer_List_Srlzr(serializers.ModelSerializer):
    customer_fullname = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = ('id_card','customer_fullname','username','email')

class PlanSerializer(serializers.ModelSerializer):
    plan_speed = serializers.ReadOnlyField()

    class Meta:
        model = Plan
        exclude = ('i_speed',)

class Contract_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'