from django.db import models

# Create your models here.


class Politician(models.Model):
    name = models.CharField(max_length=255)
    party = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    district = models.CharField(max_length=255)


class Stock(models.Model):
    symbol = models.CharField(max_length=255)
    company = models.CharField(max_length=255)


class Transaction(models.Model):
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    TRANSACTION_TYPES = [
        ('Buy', 'Buy'),
        ('Sell', 'Sell'),
        ('Dividend', 'Dividend'),
    ]
    transaction_type = models.CharField(
        max_length=255, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
