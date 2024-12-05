from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserViewSet, ProductViewSet, CategoryViewset, OrderViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"products", ProductViewSet)
router.register(r"categories", CategoryViewset)
router.register(r"orders", OrderViewSet)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
