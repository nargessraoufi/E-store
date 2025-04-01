# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .models import Cart, CartItem
# from .serializers import CartSerializer, CartItemSerializer
# from products.models import Product

# class CartViewSet(viewsets.ModelViewSet):
#     serializer_class = CartSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get_queryset(self):
#         return Cart.objects.filter(user=self.request.user)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    
#     @action(detail=True, methods=['post'])
#     def add_item(self, request, pk=None):
#         cart = self.get_object()
#         product_id = request.data.get('product_id')
#         quantity = request.data.get('quantity', 1)
        
#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return Response(
#                 {'error': 'Product not found'}, 
#                 status=status.HTTP_404_NOT_FOUND
#             )
        
#         cart_item, created = CartItem.objects.get_or_create(
#             cart=cart,
#             product=product,
#             defaults={'quantity': quantity}
#         )
        
#         if not created:
#             cart_item.quantity += int(quantity)
#             cart_item.save()
        
#         serializer = CartItemSerializer(cart_item)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     @action(detail=True, methods=['post'])
#     def checkout(self, request, pk=None):
#         cart = self.get_object()
#         # منطق ثبت سفارش اینجا پیاده‌سازی می‌شود
#         return Response({'message': 'Checkout completed'})