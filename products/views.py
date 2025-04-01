from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'brand', 'model', 'sku']
    ordering_fields = ['price', 'rating', 'created_at']

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # فیلترهای سفارشی
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
            
        min_price = self.request.query_params.get('min_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
            
        max_price = self.request.query_params.get('max_price')
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset
    
    

            
    def get (request):
        products = products.objects.all()
        serializer = ProductSerializer(products, many= True)
        return Response (serializer.data)





# @api_view(['GET'])
# def post_detail(request,post_id):
#     post = Post.objects.get(pk= post_id)
#     comments = Comment.objects.filter(post=post)
#     # context = {'post':post,'comments':comments}
#     # return render(request, 'posts/post_detail.html',context= context)
#     serializer = PostSerializer(post)
#     return Response (serializer.data)


# @api_view(['POST'])
# def create_post(request):
#     serializer = PostSerializer(data= request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"status": "ok"})
#     return Response(serializer.errors, 400)
            
