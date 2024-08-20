from django.shortcuts import render
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def catalog(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products_list = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)
    
    paginator = Paginator(products_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        products = paginator.page(page_number)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        products = paginator.page(1)

    return render(
        request,
        'goods/catalog.html',
        {
            'category': category,
            'categories': categories,
            'products': products
        }
    )   


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'goods/product_detail.html', {'product': product})