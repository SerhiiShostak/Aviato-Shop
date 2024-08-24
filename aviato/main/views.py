from django.shortcuts import render
from goods.models import Category, Product
# Create your views here.


def index(request):
    categories = Category.objects.all()[:4]
    trending_products = Product.objects.order_by('-created')[:5]

    return render(request, 'main/index.html', {'trending_products': trending_products, 'categories': categories})