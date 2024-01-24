from .models import Product
from scraper.scraper.sears_scraper import scrape_product_info
from celery import shared_task


@shared_task
def scrape_sears(product_ids):
    for product_id in product_ids:
        existing_product = Product.objects.filter(product_id=product_id).first()

        if not existing_product:
            product_info = scrape_product_info(product_id)
            if product_info is not None:
                Product.objects.create(**product_info)


@shared_task
def scrape_sears_update_data():
    existing_products = Product.objects.all()

    for product in existing_products:
        product_info = scrape_product_info(product.product_id)

        if product_info is not None:
            for key, value in product_info.items():
                setattr(product, key, value)

            product.save()

