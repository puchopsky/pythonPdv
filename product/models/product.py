from django.db import models
import uuid


class Product(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    barCode = models.CharField(max_length=100, unique=True)
    sku = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    createdOn = models.DateTimeField(blank=True)
    canceledOn = models.DateTimeField(blank=True)
    deactivatedOn = models.DateTimeField(blank=True)
    status = models.CharField(max_length=30, default='Active')
    provider = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
