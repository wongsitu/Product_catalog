from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Artist(models.Model):
    _id = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_active = models.BooleanField(default=True)
    is_visibility = models.BooleanField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    price_offer = models.DecimalField(max_digits=100, decimal_places=2,blank=True)
    offer_day_from = models.DateTimeField(blank=True)
    offer_day_to = models.DateTimeField(blank=True)
    quantity = models.IntegerField()
    sku = models.IntegerField()
    product_id = models.PositiveSmallIntegerField()

    def __str__(self):
        return self._id