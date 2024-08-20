from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<slug:category_slug>/', views.catalog, name='catalog_with_slug'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]