from django.contrib import admin

from .models import Product, ProductImage, Restaurant, Vendor


class ProductAdmin(admin.ModelAdmin):
    list_display = (
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
    list_filter = ("restaurant",)
    search_fields = ("name", "description", "ingredients")


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "name", "description", "image")
    list_filter = ("product",)
    search_fields = ("name", "description")


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "address")


class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone_number", "email", "website")
    search_fields = ("name", "address", "phone_number", "email", "website")


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Vendor, VendorAdmin)
