from django.contrib import admin
from StockSearch.models import Stock_Information
# Register your models here.

class Stock_InformationAdmin(admin.ModelAdmin):
    list_display = ('stock_year', 'stock_month', 'stock_day' ,'stock_code', 'stock_name', 'stock_capacity', 'stock_turnover', 'stock_open', 'stock_high', 'stock_low', 'stock_close','stock_change', 'stock_transaction')

admin.site.register(Stock_Information,Stock_InformationAdmin)
