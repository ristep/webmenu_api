from rest_framework import routers

from .views import ProductImageViewSet, ProductViewSet, RestaurantViewSet, VendorViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'product-images', ProductImageViewSet)
urlpatterns = router.urls
