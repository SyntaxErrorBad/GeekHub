import logging

from django.shortcuts import render, redirect
from .forms import AddProductsForm
from .models import Product
from .tasks import scrape_sears
#from  .tasks import scrape_sears_update_data

from itertools import chain





def basic_page(request):
    return redirect('my_products')


def add_products(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AddProductsForm(request.POST)
            if form.is_valid():
                product_ids = form.cleaned_data['product_ids'].split()
                scrape_sears.delay(product_ids)
                return redirect('my_products')
        else:
            form = AddProductsForm()

        return render(request, 'manageproducts/add_products.html', {'form': form})
    else:
        return redirect('my_products')


def my_products(request):
    #scrape_sears_update_data.delay()
    products = Product.objects.all()
    categories = Product.objects.values('category').distinct()
    categories = set(chain(*[(category['category']).split(",") for category in categories]))
    return render(request, 'manageproducts/my_products.html', {
        'products': products,
        'categories': categories,
    })


def category_page(request, category):
    categories = Product.objects.values('category').distinct()
    categories = set(chain(*[(category['category']).split(",") for category in categories]))
    products = Product.objects.filter(category__contains=category)
    return render(request, 'manageproducts/categories_page.html', {
        'categories': categories,
        'products': products,
    })


def product_detail(request, product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        return render(request, 'manageproducts/product_detail.html', {'product': product})
    except Exception as e:
        logging.error(f"Function {product_detail.__name__} error {e}")
        return redirect('exeption_page')


def exeption_page(request):
    return render(request, 'manageproducts/exeption_page.html')

