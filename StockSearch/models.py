from django.db import models

# Create your models here.
class Stock_Information(models.Model):
    stock_code = models.DecimalField(max_digits = 5,decimal_places=0)
    stock_name = models.CharField(max_length=20)
    stock_year = models.DecimalField(max_digits = 5,decimal_places=0)
    stock_month = models.DecimalField(max_digits = 2,decimal_places=0)
    stock_day = models.DecimalField(max_digits = 3,decimal_places=0)
    stock_capacity = models.DecimalField(max_digits = 50,decimal_places=0)
    stock_turnover = models.DecimalField(max_digits = 50,decimal_places=0)
    stock_open = models.DecimalField(max_digits = 20, decimal_places=1)
    stock_high = models.DecimalField(max_digits = 20, decimal_places=1)
    stock_low = models.DecimalField(max_digits = 20, decimal_places=1)
    stock_close = models.DecimalField(max_digits = 20, decimal_places=1)
    stock_change =  models.SmallIntegerField()
    stock_transaction = models.DecimalField(max_digits = 50,decimal_places=0)
    def __int__(self):
        return self.stock_code