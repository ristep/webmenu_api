from rest_framework import serializers

from .models import Product, ProductImage, Restaurant, Vendor


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "ingredients",
            "is_vegetarian",
            "is_vegan",
            "is_gluten_free",
            "is_natural",
            "is_drink",
            "contain_alcohol",
            "preparation_time",
            "tax_by_quantity",
            "tax_by_price",
            "restaurant",
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            "product",
            "name",
            "description",
            "image",
        )


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            "name",
            "address",
        )


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            "name",
            "address",
            "phone_number",
            "email",
            "website",
        )
