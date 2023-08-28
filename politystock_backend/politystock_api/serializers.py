from rest_framework import serializers
from .models import Politician, Stock, Transaction


class PoliticianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Politician
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
