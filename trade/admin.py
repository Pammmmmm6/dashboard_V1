from django.contrib import admin
from trade.models import Trade, Category


class TradeAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('date', 'assets')


admin.site.register(Trade, TradeAdmin)
admin.site.register(Category)
