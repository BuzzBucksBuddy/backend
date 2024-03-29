from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingOptions, SavingProducts
from django.contrib.auth import get_user_model


class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)


class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'


class OneDepOptSerializer(serializers.ModelSerializer):
    class DepositProductsSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositProducts
            fields = '__all__'
    
    product = DepositProductsSerializer(read_only=True)

    class Meta:
        model = DepositOptions
        fields = '__all__'


class OneSavOptSerializer(serializers.ModelSerializer):
    class SavingProductsSerializer(serializers.ModelSerializer):
        class Meta:
            model = SavingProducts
            fields = '__all__'
    
    product = DepositProductsSerializer(read_only=True)

    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)