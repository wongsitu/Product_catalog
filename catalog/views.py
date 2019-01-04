from django.shortcuts import render, redirect
from .models import User, Product
from catalog.forms import UserForm, ProductForm
from django.db.models import Q
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, 'catalog/all_products.html', {'products':products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            if Product.objects.last():
                product._id = Product.objects.last().id + 1
            else:
                product._id = 1
            product.save()
            return redirect('all_products')
        else:
            print('\nform is invalid\n')
    else:
        form = ProductForm()
    return render(request, 'catalog/create_product.html', {'form': form })

def product_detail(request, pk):
    product = Product.objects.get(_id=pk)
    return render(request, 'catalog/product_detail.html',{'product':product})

def search(request):
    query = request.GET.get('q')
    searched_products = Product.objects.filter(Q(_id__icontains=query))
    content = {
        'searched_products': searched_products 
        }
    return render(request, 'catalog/searchpage.html',content)

def delete_product(request, pk):
    Product.objects.get(id=pk).delete()
    return redirect('all_products')