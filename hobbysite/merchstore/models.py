from django.db import models
from django.utils import timezone
from django.urls import reverse

from user_management.models import Profile

# Create your models here.

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    

class Product(models.Model):
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('On sale', 'On sale'),
        ('Out of stock', 'Out of stock')
    )

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        null=True,
        on_delete=models.SET_NULL,
        related_name='products'
        )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    stock = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to='media/merchstore_products/', null=True, blank=True)    


    class Meta:
        ordering = ['name']


    def get_absolute_url(self):
        return reverse("merchstore:product_detail", args=[self.pk])
    

    def __str__(self):
        return f"{self.name} -- {self.product_type} -- {self.owner.user.username}"


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('On cart', 'On cart'),
        ('To pay', 'To pay'),
        ('To ship', 'To ship'),
        ('To receive', 'To receive'),
        ('Delivered', 'Delivered')
    )

    buyer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )
    amount = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_on = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.product.name} -- {self.buyer.user.username} (buyer) -- {self.product.owner} (seller)"
