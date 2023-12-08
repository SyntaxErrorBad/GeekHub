# 2. Створіть програму для отримання курсу валют за певний період. 
# - отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте
# механізм реалізації) і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних
import datetime
import requests


def is_valid_date(date):
    try:
        datetime.datetime.strptime(date, "%d.%m.%Y")
        today = datetime.datetime.now().date().strftime("%d.%m.%Y")
        if today >= date:
            return True, date
        return False, None
    except Exception as e:
        return False, e


def is_valid_currency(prompt):
        input_prompt = input(prompt)
        currenc = ["USD", "EUR", "GBP", "JPY", "CHF", "CNY"]
        if input_prompt in currenc:
            return True, input_prompt
        else:
            return False, "Неправильна валюта. Дозволені валюти: USD, EUR, GBP, JPY, CHF, CNY"


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
    date_current_input = input("Бажаєте за переіод?\nТак(1)\nНі(2)\nДля виходу(3):")
    if date_current_input == "2":
        valid_date, date = is_valid_date(
            input("Введіть дату (DD-MM-YYYY) обов'язково з 0 якщо одиничне число(наприклад 08): "))
        valid_currency, currency = is_valid_currency("Введіть валюту (USD, EUR, GBP, JPY, CHF, CNY): ")
        if valid_date is True and valid_currency is True:
            rate_sale, rate_purchase = get_rate(date, currency)
            if rate_sale is not None:
                print("Курс продажу {} на {} становить {} гривень.".format(currency, date, rate_sale))
                print("Курс покупки {} на {} становить {} гривень.".format(currency, date, rate_purchase))
            else:
                print("Немає даних про курс {} на {}.".format(currency, date))
        else:
            print("Введені неправильні дані!")
        
        main()
    elif date_current_input == "1":
        valid_start_date, start_date = is_valid_date(input("Введіть початкову дату (DD-MM-YYYY): "))
        valid_end_date, end_date = is_valid_date(input("Введіть кінцеву дату (DD-MM-YYYY): "))
        if valid_start_date is True and valid_end_date is True:
            valid_currency, currency = is_valid_currency("Введіть валюту (USD, EUR, GBP, JPY, CHF, CNY): ")
            if valid_currency is True:
                start_rate_sale, start_rate_purchase = get_rate(start_date, currency)
                end_rate_sale, end_rate_purchase = get_rate(end_date, currency)
                if start_rate_sale is not None and end_rate_sale is not None:
                    print("Курс продажу {} на {} становить {} гривень.".format(currency, start_date, start_rate_sale))
                    print("Курс покупки {} на {} становить {} гривень.".format(currency, start_date,
                                                                               start_rate_purchase))
                    print("_"*50)
                    print("Курс продажу {} на {} становить {} гривень.".format(currency, end_date, end_rate_sale))
                    print("Курс покупки {} на {} становить {} гривень.".format(currency, end_date, end_rate_purchase))
                    print("_"*50)
                    print(f"Різниця між продажом за {start_date} та між {end_date}: {end_rate_sale - start_rate_sale}")
                else:
                    print("Немає даних про курс {} на {} і {}.".format(currency, start_date, end_date))

            else:
                print("Невірна валюта")
        else:
            print("Невірна дата")
            
        main()
    
    elif date_current_input == "3":
        exit()
    else:
        main()


if __name__ == "__main__":
    main()
    
