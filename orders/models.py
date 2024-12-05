from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):

    ORDER_STATUSES = [
        ("pending", "pending"),
        ("completed", "completed"),
        ("delivered", "delivered"),
    ]

    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="orders"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="orders"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=ORDER_STATUSES, default="pending", max_length=20)
