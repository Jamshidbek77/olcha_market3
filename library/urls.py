from django.urls import path
from library.views import (
    HomeView,
    ProductView, DetailProductView, CreateProductView,
    ShopView, DetailShopView, CreateShopView,
    UserView, DetailUserView, CreateUserView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product', ProductView.as_view(), name='product'),
    path('product/create', CreateProductView.as_view(), name='create_product'),
    path('product/<int:pk>', DetailProductView.as_view(), name='product_detail'),
    path('shops', ShopView.as_view(), name='shops'),
    path('shops/create', CreateShopView.as_view(), name='create_shop'),
    path('shops/<int:pk>', DetailShopView.as_view(), name='shop'),
    path('users', UserView.as_view(), name='users'),
    path('users/create', CreateUserView.as_view(), name='create_user'),
    path('users/<int:pk>', DetailUserView.as_view(), name='user'),
]