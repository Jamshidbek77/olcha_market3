from django.shortcuts import render, redirect
from django.views import View
from .models import User, Product, Shop
from .forms import ShopForm, ProductForm, UserForm


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product/product.html', {'products': products})


class DetailProductView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product/detail_product.html', {'product': product})


class CreateProductView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'product/create_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
        return render(request, 'product/create_product.html', {'form': form})


class ShopView(View):
    def get(self, request):
        shops = Shop.objects.all()
        return render(request, 'shop/shop.html', {'shops': shops})


class DetailShopView(View):
    def get(self, request, pk):
        shop = Shop.objects.get(pk=pk)
        return render(request, 'shop/detail_shop.html', {'shop': shop})


class CreateShopView(View):
    def get(self, request):
        form = ShopForm()
        return render(request, 'shop/create_shop.html', {'form': form})

    def post(self, request):
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shops')
        return render(request, 'shop/create_shop.html', {'form': form})


class UserView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user/user.html', {'users': users})


class DetailUserView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return render(request, 'user/detail_user.html', {'user_obj': user})


class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user/create_user.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(request, 'user/create_user.html', {'form': form})