from django.db import models
import uuid


class SaleForm(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # This field specifies wether the producto is sold by box, unit, hanlfbox, liters, etc
    form = models.CharField(max_length=50, default='Unit')

    # This filed sets an equivalent on how many units needs to be discounted from the stock, ex. If a box contains 12
    # units then 12 units needs to be removed from the stock
    totalUnitsInFromSale = models.FloatField(default=1.0)
