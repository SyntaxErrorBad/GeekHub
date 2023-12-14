import requests
import csv
import os


current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)


def write_data_to_csv(data, category_id):
    with open(os.path.join(parent_directory, f'{category_id}.csv'), "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        for dt in data:
            writer.writerow(dt)


def get_products_by_category_page(category_id,url = None,count = 0):
    cookies = {
        '__cf_bm': 'zNqVBwj2HKPqp00S6eGD1mbyjefAlyzdWJxStAoCmLc-1702062572-1-'
                   'AZLYiXDX1iYf8jJCMbim18B9uW8Q213bluEDthWFbCF5hR9/CFjxnEWNlw'
                   'PsSiibwOr1A1/Z/sddC/lZXUTu0CeP+o7tnaeU1UJtPB51L7Jy',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Fri+Dec+08+2023+21^%^'
                          '^%^3A54+GMT^%^2B0200+(^%^D0^%^92^%^D0^%^BE^%^D1^%^81^%^'
                          'D1^%^82^%^D0^%^BE^%^D1^%^87^%^D0^%^BD^%^D0^%^B0^%^D1^%^8F+'
                          '^%^D0^%^95^%^D0^%^B2^%^D1^%^80^%^D0^%^BE^%^D0^%^BF^%^D0^%^'
                          'B0^%^2C+^%^D1^%^81^%^D1^%^82^%^D0^%^B0^%^D0^%^BD^%^D0^%^B4'
                          '^%^D0^%^B0^%^D1^%^80^%^D1^%^82^%^D0^%^BD^%^D0^%^BE^%^D0^%^'
                          'B5+^%^D0^%^B2^%^D1^%^80^%^D0^%^B5^%^D0^%^BC^%^D1^%^8F)&version=202209'
                          '.1.0&hosts=&groups=C0001^%^3A1^%^2CC0003^%^3A1^%^2CC0002^%^3A1^%^'
                          '2CC0004^%^3A1^%^2CSPD_BG^%^3A1&landingPath=NotLandingPage&geolocation=UA^%^3B71',
        'forterToken': 'd4d56131532040da8732506b2b556724_1702062572695_826_UDF43-m4_13ck',
        'irp': 'e636783c-68b0-4f20-a748-0514f1b516d0^|jct3L4tL65Lccfr1ixu^%^'
               '2BlQRI4RjDN1N2DpwKXq7DBeE^%^3D^|G^|72f75961-7df0-4d9d-8679-bf4'
               '601301775^|0^|NO_SESSION_TOKEN_COOKIE',
        'cf_clearance': 'UE8gW883O0r7GMxFljwJE7Le9ied.vXYae0uQNIzcOU-'
                        '1702062473-0-1-b88a9026.c9bbc066.5b84f0a1-0.2.1702062473',
        'zipCode': '10101',
        'city': 'New York',
        'state': 'NY',
        'initialTrafficSource': 'utmcsr=(direct)^|utmcmd=(none)^|utmccn=(not set)',
        '__utmzzses': '1',
        'ftr_blst_1h': '1702059432435',
        'ltkSubscriber-Footer': 'eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCJ9',
        'ltkpopup-session-depth': '8-2',
        'OptanonAlertBoxClosed': '2023-12-08T19:07:53.987Z',
        'ftr_ncd': '6',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        f'Referer': 'https://www.sears.com/category/b-{id}',
        'Content-Type': 'application/json',
        'Authorization': 'SEARS',
        'Alt-Used': 'www.sears.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
    }

    if url is None:
        url = (f'https://www.sears.com/api/sal/v3/products/search?startIndex=1&endIndex=48&searchType='
                f'category&catalogId=12605&store=Sears&storeId=10153&zipCode=10101&bratRedirectInd=true&cat'
                f'PredictionInd=true&disableBundleInd=true&filterValueLimit=500&includeFiltersInd=true&shipOr'
                f'Delivery=true&solrxcatRedirection=true&sortBy=ORIGINAL_SORT_ORDER&whiteListCacheLoad=false&eager'
                f'CacheLoad=true&slimResponseInd=true&catGroupId={category_id}&seoURLPath=category/{category_id}')
        
        response = requests.get(url,cookies=cookies,headers=headers)
        count = response.json()["metadata"]["count"]
        get_products_by_category_page(category_id,url=url,count=count)


    for item in range(1,count,48):
        print(f"Current items between {count} and {count + 47}"
        url = (f'https://www.sears.com/api/sal/v3/products/search?startIndex={str(item)}&endIndex={str(item+47)}&searchType='
                f'category&catalogId=12605&store=Sears&storeId=10153&zipCode=10101&bratRedirectInd=true&cat'
                f'PredictionInd=true&disableBundleInd=true&filterValueLimit=500&includeFiltersInd=true&shipOr'
                f'Delivery=true&solrxcatRedirection=true&sortBy=ORIGINAL_SORT_ORDER&whiteListCacheLoad=false&eager'
                f'CacheLoad=true&slimResponseInd=true&catGroupId={category_id}&seoURLPath=category/{category_id}')

        response = requests.get(url,cookies=cookies,headers=headers)

        if response.status_code == 200:
            take_data_from_json_to_dict(response, id)
        else:
            print(f"Виникла помилка спробуйте знову! {response.status_code}")

def take_data_from_json_to_dict(response, category_id):
    data = []
    for element in response.json()["items"]:
        brand = element["brandName"]
        name = element["name"]
        regularprice = element["price"]["regularPriceDisplay"]
        finalprice = element["price"]["finalPriceDisplay"]
        category = element["category"]
        data.append({"Brand": brand, "Name": name, "RegularPrice": regularprice, "FinalPrice": finalprice,
                     "Category": category})

    write_data_to_csv(data, category_id)


get_products_by_category_page(input("Введіть ID(лише цифри): "))
