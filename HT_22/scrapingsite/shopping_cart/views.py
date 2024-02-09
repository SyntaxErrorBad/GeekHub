from django.shortcuts import render, redirect
from .forms import ShoppingCartItemForm

from django.contrib.auth.decorators import login_required


@login_required(login_url='/my-products/')
def shopping_cart_add_item(request, product_id):
    if request.method == 'POST':
        form = ShoppingCartItemForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['quantity']
            shopping_cart = request.session.get('shopping_cart') or []
            shopping_cart.append({
                'ID': product_id,
                'Count': count
            })
            request.session['shopping_cart'] = shopping_cart
            return redirect('shopping_cart_page')

    else:
        form = ShoppingCartItemForm()

    return render(request, 'shopping_cart/shopping_cart_item_page.html', {'form': form, 'product_id': product_id})


@login_required(login_url='/my-products/')
def shopping_cart_remove_item(request, product_id):
    shopping_cart = request.session.get('shopping_cart') or []
    for item_in_cart in shopping_cart:
        if item_in_cart['ID'] == product_id:
            shopping_cart.remove(item_in_cart)
            request.session['shopping_cart'] = shopping_cart
            return redirect('my_products')

    return redirect('shopping_cart_add_item', product_id)


@login_required(login_url='/my-products/')
def shopping_cart_clear(request):
    request.session['shopping_cart'] = []
    return redirect('my_products')


@login_required(login_url='/my-products/')
def shopping_cart_page(request):
    products = request.session.get('shopping_cart')
    return render(request, 'shopping_cart/shopping_cart_page.html', {'products': products})


@login_required(login_url='/my-products/')
def shopping_cart_manipulate_one_item(request):
    products = request.session.get('shopping_cart')
    if request.method == 'POST':
        operation, item_id = (request.POST.get('operation')).split('|')
        for product in products:
            if product['ID'] == item_id:
                if operation == 'add':
                    product['Count'] += 1
                else:
                    if product['Count'] > 1:
                        product['Count'] -= 1

    request.session['shopping_cart'] = products

    return render(request, 'shopping_cart/shopping_cart_page.html', {'products': products})

