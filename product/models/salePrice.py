from django.db import models
from product.models.saleForm import SaleForm
import uuid


class SalePrice(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.FloatField(default=0.0)
    status = models.CharField(max_length=30, default='Deactivated')
    promotion = models.CharField(max_length=3, default='No')
    promotionStartsOn = models.DateTimeField(blank=True)
    promotionExpiresOn = models.DateTimeField(blank=True)
    formSale = models.ForeignKey(SaleForm, on_delete=models.DO_NOTHING)
