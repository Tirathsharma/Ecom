from rest_framework import viewsets
from .Serializers import ProductSerializer
from .models import Product

class ProductViewset(viewsets.ModelViewSet):
    queryset= Product.objects.all().order_by('id')
    serializer_class= ProductSerializer
