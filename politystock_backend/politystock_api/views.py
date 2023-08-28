from django.shortcuts import render
from rest_framework import generics
from .models import Politician, Stock, Transaction
from .serializers import PoliticianSerializer, StockSerializer, TransactionSerializer


# Create your views here.
class PoliticianList(generics.ListCreateAPIView):
    queryset = Politician.objects.all()
    serializer_class = PoliticianSerializer


class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
