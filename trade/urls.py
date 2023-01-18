from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from trade.views import index, add_trade, delete_trade

urlpatterns = [
    path('', index, name="trade"),
    path('add-trade', add_trade, name="add-trade"),
    path('delete-trade/<int:id>', delete_trade, name="delete-trade"),
]
