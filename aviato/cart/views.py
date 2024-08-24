from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from goods.models import Product
from django.views.decorators.http import require_POST
from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        if request.POST.get('product-quantity'):
            quantity = int(request.POST.get('product-quantity'))
        else:
            quantity = 1
        cart.add(product, quantity=quantity)
        messages.success(request, f'Product "{product.name}" added to cart')

    return redirect(request.META.get('HTTP_REFERER', '/'))


# Create your views here.
def cart_detail(request):
    
    return render(request, 'cart/cart_detail.html')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    messages.success(request, f'Product "{product.name}" removed from cart')

    return redirect(request.META.get('HTTP_REFERER', '/'))