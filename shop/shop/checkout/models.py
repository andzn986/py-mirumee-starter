from django.db import models
from ..product.models import ProductVariant


# Create your models here.
class Checkout(models.Model):
    user = models.ForeignKey(on_delete=models.CASCADE)
    user_email = models.EmailField()


class CheckoutLine(models.Model):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    checkout = models.ForeignKey(Checkout, related_name="lines", on_delete=models.CASCADE)
