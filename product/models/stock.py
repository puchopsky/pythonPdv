from django.db import models
from product.models.product import Product
from product.models.salePrice import SalePrice
import uuid


class Stock(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete= models.DO_NOTHING)
    amount = models.FloatField(default=0.0)
    minAmountAlertForRestock = models.FloatField(default=0.0)
    expirationDate = models.DateTimeField(blank=True)
    boughtPrice = models.FloatField(default=0.0)
    salePrice = models.ForeignKey(SalePrice, on_delete=models.DO_NOTHING)

   