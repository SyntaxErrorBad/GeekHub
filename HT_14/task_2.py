# 2. Створіть програму для отримання курсу валют за певний період. 
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних

import dateutil.parser
import requests
import datetime

def get_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            dateutil.parser.parse(date_str)
            return date_str
        except ValueError:
            print("Невірний формат дати. Введіть дату у форматі DD-MM-YYYY.")

def get_currency(prompt):
        input_prompt = input(prompt)
        currenc = ["USD", "EUR", "GBP", "JPY", "CHF", "CNY"]
        if input_prompt in currenc:
            return input_prompt
        else:
            print("Неправильна валюта. Дозволені валюти: USD, EUR, GBP, JPY, CHF, CNY")


def get_rate(date, currency):

    url = f"https://api.privatbank.ua/p24api/exchange_rates?date={date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for rate in data["exchangeRate"]:
            if rate["currency"] == currency:
                return rate["saleRateNB"], rate["purchaseRateNB"]
    return None, None

def main():
    date_current_input = input("Бажаєте за переід?\nТак(1)\nНі(2)\n:")
    if date_current_input == "2":
        date = get_date("Введіть дату (DD-MM-YYYY): ")
        currency = get_currency("Введіть валюту (USD, EUR, GBP, JPY, CHF, CNY): ")
        rate_sale,rate_purchase = get_rate(date, currency)
        if rate_sale is not None:
            print("Курс продажу {} на {} становить {} гривень.".format(currency, date, rate_sale))
            print("Курс покупки {} на {} становить {} гривень.".format(currency, date, rate_purchase))
        else:
            print("Немає даних про курс {} на {}.".format(currency, date))
    elif date_current_input == "1":
        date_format="%d.%m.%Y"
        start_date = get_date("Введіть початкову дату (DD-MM-YYYY): ")
        end_date = get_date("Введіть кінцеву дату (DD-MM-YYYY): ")
        start_date_ = datetime.datetime.strptime(start_date, date_format)
        end_date_ = datetime.datetime.strptime(end_date, date_format)
        if start_date_ < end_date_:
            currency = get_currency("Введіть валюту (USD, EUR, GBP, JPY, CHF, CNY): ")
            start_rate_sale,start_rate_purchase = get_rate(start_date, currency)
            end_rate_sale,end_rate_purchase = get_rate(end_date, currency)
            print(start_rate_sale,end_rate_sale)
            if start_rate_sale is not None and end_rate_sale is not None:
                print("Курс продажу {} на {} становить {} гривень.".format(currency, start_date, start_rate_sale))
                print("Курс покупки {} на {} становить {} гривень.".format(currency, start_date, start_rate_purchase))
                print("_"*50)
                print("Курс продажу {} на {} становить {} гривень.".format(currency, end_date, end_rate_sale))
                print("Курс покупки {} на {} становить {} гривень.".format(currency, end_date, end_rate_purchase))
                print("_"*50)
                print(f"Різниця між продажом за {start_date} між {end_date}: {end_rate_sale - start_rate_sale}")
            else:
                print("Немає даних про курс {} на {} і {}.".format(currency, start_date,end_date))

        else:
            print("спробуйте знову")
    else:
        print("Неправильні дані")
    main()

if __name__ == "__main__":
    main()