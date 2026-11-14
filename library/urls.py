from django.urls import path
from library.views import HomeView, ProductView, ShopView, UserView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product', ProductView.as_view(), name='product'),
    path('shops', ShopView.as_view(), name='shops'),
    path('users', UserView.as_view(), name='users'),
]
