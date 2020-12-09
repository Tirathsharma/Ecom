from rest_framework import viewsets
from .Serializers import CategorySerializer
from .models import category

class categoryViewset(viewsets.ModelViewSet):
    queryset= category.objects.all().order_by('name')
    serializer_class= CategorySerializer