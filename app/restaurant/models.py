from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.TextField()
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_natural = models.BooleanField(default=False)
    is_drink = models.BooleanField(default=False)
    contain_alcohol = models.BooleanField(default=False)
    preparation_time = models.IntegerField()  # Time in minutes
    tax_by_quantity = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    tax_by_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.RESTRICT)
    lookup_field = "id"

    ts_create = models.DateTimeField(auto_now_add=True)
    ts_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.RESTRICT
    )
    name = models.CharField(max_length=32, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="Product_images/")
    lookup_field = "id"

    ts_create = models.DateTimeField(auto_now_add=True)
    ts_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # You can add more fields like opening hours, contact information, etc.

    ts_create = models.DateTimeField(auto_now_add=True)
    ts_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()
    website = models.URLField()

    ts_create = models.DateTimeField(auto_now_add=True)
    ts_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
