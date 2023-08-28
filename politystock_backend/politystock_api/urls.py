from django.urls import path
from .views import PoliticianList, StockList, TransactionList


urlpatterns = [
    path('politicians/', PoliticianList.as_view(), name='politician-list'),
    path('stocks/', StockList.as_view(), name='stock-list'),
    path('transactions/', TransactionList.as_view(), name='transaction-list'),
]
