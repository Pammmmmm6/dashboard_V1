from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

ACTION_CHOICES = [
    ('LONG', 'LONG'),
    ('SHORT', 'SHORT'),
]
STATUS_CHOICES = [
    ('LOSE', 'LOSE'),
    ('WIN', 'WIN'),
]
MARKET_CHOICES = [
    ('FOREX', 'FOREX'),
    ('STOCK', 'STOCK'),
    ('CRYPTO', 'CRYPTO'),
    ('FUTURES', 'FUTURES'),
    ('OPTIONS', 'OPTIONS'),
    ('NONE', 'NONE')
]
TYPES_CHOICES = [
    ('SWING TRADE', 'SWING TRADE'),
    ('SCALPING', 'SCALPING'),
]


class Trade(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, default=0)
    date = models.DateField(default=now)
    category = models.CharField(max_length=32, choices=MARKET_CHOICES)
    assets = models.CharField(max_length=16)
    action = models.CharField(max_length=32, choices=ACTION_CHOICES)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    types = models.CharField(max_length=32, choices=TYPES_CHOICES)
    risk = models.IntegerField(default=1)
    profit = models.DecimalField(max_digits=16, decimal_places=2)
    balance = models.DecimalField(max_digits=16, decimal_places=2)
    setup = models.URLField(max_length=132, blank=True)

    def __str__(self):
        return f'{self.owner.username} | {self.date} | {self.assets}'

    class Meta:
        ordering: ['-date']


class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
