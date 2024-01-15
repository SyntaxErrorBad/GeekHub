import logging

from django.shortcuts import render, redirect
from .forms import AddProductsForm, ShoppingCartItemForm
from .models import Product
from .tasks import scrape_sears, scrape_sears_update_data


def basic_page(request):
    return redirect('my_products')


def add_products(request):
    if request.method == 'POST':
        form = AddProductsForm(request.POST)
        if form.is_valid():
            product_ids = form.cleaned_data['product_ids'].split()
            scrape_sears(product_ids)
            return redirect('my_products')
    else:
        form = AddProductsForm()

    return render(request, 'manageproducts/add_products.html', {'form': form})


def my_products(request):
    scrape_sears_update_data()
    products = Product.objects.all()
    return render(request, 'manageproducts/my_products.html', {'products': products})


def product_detail(request, product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        return render(request, 'manageproducts/product_detail.html', {'product': product})
    except Exception as e:
        logging.error(f"Function {product_detail.__name__} error {e}")
        return redirect('exeption_page')


def exeption_page(request):
    return render(request, 'manageproducts/exeption_page.html')


def shopping_cart_add_item(request, product_id):
    if request.method == 'POST':
        form = ShoppingCartItemForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['quantity']
            shopping_cart = request.session.get('shopping_cart') or []
            shopping_cart.append({
                "ID": product_id,
                "Count": count
            })
            request.session['shopping_cart'] = shopping_cart
            return redirect("shopping_cart_page")

    else:
        form = ShoppingCartItemForm()

    return render(request, 'manageproducts/shopping_cart_item_page.html', {'form': form, 'product_id': product_id})


def shopping_cart_remove_item(request, product_id):
    shopping_cart = request.session.get('shopping_cart') or []
    for item_in_cart in shopping_cart:
        if item_in_cart["ID"] == product_id:
            shopping_cart.remove(item_in_cart)
            request.session['shopping_cart'] = shopping_cart
            return redirect("my_products")

    return redirect("shopping_cart_add_item", product_id)


def shopping_cart_clear(request):
    request.session['shopping_cart'] = []
    return redirect("my_products")


def shopping_cart_page(request):
    products = request.session.get("shopping_cart")
    return render(request, 'manageproducts/shopping_cart_page.html', {'products': products})


def shopping_cart_manipulate_one_item(request):
    products = request.session.get("shopping_cart")
    if request.method == 'POST':
        operation, item_id = (request.POST.get('operation')).split('|')
        for product in products:
            if product['ID'] == item_id:
                if operation == 'add':
                    product['Count'] += 1
                else:
                    if product['Count'] > 1:
                        product['Count'] -= 1

    request.session["shopping_cart"] = products

    return render(request, 'manageproducts/shopping_cart_page.html', {'products': products})
