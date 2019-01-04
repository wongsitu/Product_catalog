from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_products, name="all_products"),
    path('products/<int:pk>/', views.product_detail, name="product_detail"),
    path('products/create_product/', views.create_product, name="create_product"),
    path('products/<int:pk>/edit', views.product_edit, name="product_edit"),
    path('products/<int:pk>/delete', views.delete_product, name="delete_product"),
    path('search', views.search, name="search"),
    path('register', views.register, name='register'),
    path('login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name='logout'),
]