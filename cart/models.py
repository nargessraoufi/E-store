# from django.db import models
# from products.models import Product
# # from user.models import User

# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     @property
#     def total_items(self):
#         return self.items.count()

#     @property
#     def subtotal(self):
#         return sum(item.total_price for item in self.items.all())

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)

#     @property
#     def total_price(self):
#         return self.product.price * self.quantity

#     def __str__(self):
#         return f"{self.quantity} x {self.product}"