from django.shortcuts import render
from django.views import View
from .models import User, Product, Shop


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product/product.html', {'products': products})


class ShopView(View):
    def get(self, request):
        shops = Shop.objects.all()
        return render(request, 'shop/shop.html', {'shops': shops})


class UserView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user/user.html', {'users': users})