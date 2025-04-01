# from rest_framework import serializers
# from products.serializers import ProductSerializer
# from .models import Cart, CartItem

# class CartItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer()
#     total_price = serializers.SerializerMethodField()
    
#     class Meta:
#         model = CartItem
#         fields = ['id', 'product', 'quantity', 'total_price']
    
#     def get_total_price(self, obj):
#         return obj.total_price

# class CartSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True, read_only=True)
#     subtotal = serializers.SerializerMethodField()
#     total_items = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Cart
#         fields = ['id', 'items', 'total_items', 'subtotal', 'created_at', 'updated_at']
    
#     def get_subtotal(self, obj):
#         return obj.subtotal
    
#     def get_total_items(self, obj):
#         return obj.total_items