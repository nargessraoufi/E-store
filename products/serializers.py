
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'brand', 'model', 'category', 
            'storage', 'color', 'sku', 'price', 'discount',
            'final_price', 'rating', 'stock', 'screen_diagonal',
            'screen_type', 'battery_capacity', 'protection_class'
        ]
    
    def get_final_price(self, obj):
        return obj.price * (1 - obj.discount / 100)