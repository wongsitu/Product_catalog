from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_products, name="all_products"),
    path('products/<int:pk>/', views.product_detail, name="product_detail"),
    path('products/create_product/', views.create_product, name="create_product"),
    path('products/<int:pk>/delete', views.delete_product, name="delete_product"),
    path('search', views.search, name="search"),
]