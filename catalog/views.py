from django.shortcuts import render, redirect
from .models import User, Product
from catalog.forms import UserForm, ProductForm
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# Show all
def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products,8)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'catalog/all_products.html', {'products':products})

# Create
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

# Show one
def product_detail(request, pk):
    product = Product.objects.get(_id=pk)
    return render(request, 'catalog/product_detail.html',{'product':product})

# Edit
def product_edit(request,pk):
    product = Product.objects.get(_id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.modified = timezone.datetime.now()
            product.save()
            return redirect('all_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/product_edit.html', {'form': form, 'product': product})

# Search
def search(request):
    query = request.GET.get('q')
    searched_products = Product.objects.filter(Q(_id=query))
    content = {
        'searched_products': searched_products 
        }
    return render(request, 'catalog/searchpage.html',content)

# Delete one
def delete_product(request, pk):
    Product.objects.get(id=pk).delete()
    return redirect('all_products')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Thanks for joining')
            registered = True
            login(request, user)
            return redirect('all_products')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'catalog/registration.html', {'user_form':user_form,'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have logged out')
    return redirect('all_products')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.success(request, 'You have logged in successfully')
                return redirect('all_products')
            else:
                messages.warning(request,"Your account was inactive.")
                return redirect('user_login')
        else:
            messages.warning(request,"Invalid login details given")
            return redirect('user_login')
    else:
        return render(request, 'catalog/login.html')