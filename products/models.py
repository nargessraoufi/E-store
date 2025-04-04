from django.db import models

class Product(models.Model):
    PRODUCT_CATEGORIES = [
        ('PHONE', 'Smartphone'),
        ('CAMERA', 'Camera'),
        ('WATCH', 'Smartwatch'),
        ('HEADPHONE', 'Headphone'),
        ('COMPUTER', 'Computer'),
        ('GAMING', 'Gaming'),
    ]
    
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=PRODUCT_CATEGORIES)
    storage = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    

    # مشخصات فنی
    screen_diagonal = models.CharField(max_length=20, blank=True)
    screen_type = models.CharField(max_length=50, blank=True)
    battery_capacity = models.CharField(max_length=20, blank=True)
    protection_class = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} {self.storage} {self.color}"

    class Meta:
        ordering = ['-created_at']


