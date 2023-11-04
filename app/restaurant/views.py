from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import Product, ProductImage, Restaurant, Vendor
from .serializers import ProductSerializer, ProductImageSerializer, RestaurantSerializer, VendorSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

    @action(methods=['get'], detail=False)
    def top_cheap(self, request):
        list = self.get_queryset().order_by('price')
        top_cheap = list.first()
        two_runners = list[1:3]
        serializer = self.get_serializer_class()(top_cheap, many=False, context={'request': request})
        cheapest_two_serializer = self.get_serializer_class()(two_runners, many=True, context={'request': request})
        return Response({
            'top_cheapest': serializer.data,
            'two_runners': cheapest_two_serializer.data
        })


class ProductImageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class VendorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
