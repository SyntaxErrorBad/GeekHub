import logging
import requests
from urllib.parse import urljoin
from .scraper_data import params, cookies, headers

logger = logging.getLogger(__name__)


def scrape_product_info(product_id):
    response = requests.get(
        f'https://www.sears.com/api/sal/v3/products/details/{product_id}',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    try:
        products = response.json()["productDetail"]["softhardProductdetails"][0]
        product_info = {
            'product_id': product_id,
            'name': products['descriptionName'],
            'price': products['salePrice'],
            'description': products['topDescription'],
            'brand': products['brandName'],
            'category': ','.join([i['name'] for i in products['hierarchies']['specificHierarchy']]),
            'sears_link': urljoin("https://www.sears.com/", products['seoUrl']),
            'img': products['mainImageUrl']
        }

    except Exception as e:
        logger.error(f"Function {scrape_product_info.__name__} has a problem {e}")
        product_info = None

    return product_info