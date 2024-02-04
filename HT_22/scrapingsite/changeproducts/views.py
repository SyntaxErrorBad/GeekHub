from django.shortcuts import render, get_object_or_404, redirect
from manageproducts.models import Product
from .forms import ProductEditForm
from django.contrib.auth.decorators import user_passes_test

from scraper.scraper.sears_scraper import scrape_product_info


@user_passes_test(lambda user: user.is_superuser, login_url='/my-products/')
# Create your views here.
def change_info_product(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            if request.POST.get('action') == 'update':
                form.save()
            elif request.POST.get('action') == 'delete':
                product.delete()
                return redirect('my_products')
            elif request.POST.get('action') == 'refresh':
                Product.objects.filter(product_id=product_id).update(
                    **scrape_product_info(product_id=product_id)
                )
            return redirect('product_detail', product_id = product_id)
    else:
        form = ProductEditForm(instance=product)

    return render(request, 'changeproducts/changeinfoproduct.html', {'form': form, 'product': product})
