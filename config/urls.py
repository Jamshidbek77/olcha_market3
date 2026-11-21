from django.urls import path
from library.views import (
    HomeView,
    ProductView,
    ShopView, DetailShopView, CreateShopView,
    UserView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product', ProductView.as_view(), name='product'),
    path('shops', ShopView.as_view(), name='shops'),
    path('shops/<int:pk>', DetailShopView.as_view(), name='shop'),
    path('shops/create', CreateShopView.as_view(), name='create_shop'),
    path('users', UserView.as_view(), name='users'),
]