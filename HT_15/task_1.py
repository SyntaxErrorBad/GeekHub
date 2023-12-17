import requests
import csv
import os
import time

current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)

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


def params(category_id,start_id = 1,end_id = 48):
    params = {
        'startIndex': str(start_id),
        'endIndex': str(end_id),
        'searchType': 'category',
        'catalogId': 12605,
        'store': 'Sears',
        'storeId': 10153,
        'zipCode': 10101,
        'bratRedirectInd': True,
        'catPredictionInd': True,
        'disableBundleInd': True,
        'filterValueLimit': 500,
        'includeFiltersInd': True,
        'shipOrDelivery': True,
        'solrxcatRedirection': True,
        'sortBy': 'ORIGINAL_SORT_ORDER',
        'whiteListCacheLoad': False,
        'eagerCacheLoad': True,
        'slimResponseInd': True,
        'catGroupId': category_id,
        'seoURLPath': f'tools-tool-storage/{str(category_id)}',
    }
    return params

def take_page_from_website(category_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Linux i585 x86_64; en-US) Gecko/20100101 Firefox/51.2',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': f'https://www.sears.com/category/b-{category_id}',
        'Content-Type': 'application/json',
        'Authorization': 'SEARS',
        'Alt-Used': 'www.sears.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
    }



    url = "https://www.sears.com/api/sal/v3/products/search"
    offset_new = 48
    limit_new = 1
    response_json_items = [""]
    while len(response_json_items) != 0:
        response = requests.get(url,cookies=cookies,headers=headers,params=params(category_id=category_id,start_id=limit_new,end_id=offset_new))
        if response.status_code == 200:
            response_json_items = response.json()["items"]
            offset_new = int(response.json()["metadata"]["offset"]) + len(response_json_items)
            limit_new = int(response.json()["metadata"]["limit"]) + len(response_json_items)
            take_data_from_json_to_dict(response,category_id)
            time.sleep(1)
            print(f"start index of items: {limit_new}")

        elif response.status_code == 504:
            print(f"Responce: {response.status_code}")
            time.sleep(1)
        else:
            print(f"Виникла помилка {response.status_code}")
            response_json_items = []
            

def write_data_to_csv(data, category_id):
    file_name = os.path.join(parent_directory, f'{category_id}.csv')
    if os.path.exists(file_name):
        with open(file_name, 'a+', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            for dt in data:
                writer.writerow(dt)

    else:
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            for dt in data:
                writer.writerow(dt)


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


take_page_from_website(input("Введіть ID(лише цифри): "))
