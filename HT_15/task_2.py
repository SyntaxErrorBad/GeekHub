import requests
from bs4 import BeautifulSoup
import os
import csv
import time
import random
from urllib.parse import urljoin


current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)


def write_data_to_csv(data):
    with open(os.path.join(parent_directory, 'data.csv'), "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        if csvfile.tell() == 0:
            writer.writeheader()
        for dt in data:
            writer.writerow(dt)


def register_on_site():
    data = {
        'login': 'Test1112',
        'password': 'Test2020'
    }

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'
    }
    session = requests.Session()
    url = "https://www.expireddomains.net/logincheck/"
    session.post(url, data=data, headers=header)
    return session, header


def take_page(session, header, url=None):
    if url is None:
        url = "https://member.expireddomains.net/domains/expiredcom/"
    time.sleep(random.randint(0, 10))
    response = session.get(url=url, headers=header)
    if response.status_code == 200:
        print(f"Current url: {url}")
        next_page = pars_pages(response)
        if next_page is None:
            print("Program Finished!")
            exit()
        else:
            take_page(session=session, header=header, url=urljoin("https://member.expireddomains.net", next_page))
    else:
        print("Something Wrong!")


def pars_table(soup):
    data = []
    if soup.select_one("table.base1") is None:
        return None
    else:
        tbody = soup.select_one("tbody")
        trs = tbody.select("tr")
        for tr in trs:
            field_domain = tr.select_one("td.field_domain").text
            field_adddate = tr.select_one("td.field_adddate").text
            field_whois = tr.select_one("td.field_whois").text
            field_creationdate = tr.select_one("td.field_creationdate").text
            data.append({"field_domain": field_domain, "field_adddate": field_adddate,
                         "field_whois": field_whois, "field_creationdate": field_creationdate})
        return data


def pars_pages(response):
    soup = BeautifulSoup(response.content, 'lxml')

    next_page = soup.select_one("a.next")
    pars_table_data = pars_table(soup)
    if pars_table_data is None:
        return None
    
    write_data_to_csv(data=pars_table_data)

    if next_page is None:
        return None
    else:
        return next_page["href"]


def main():
    session, header = register_on_site()
    take_page(session=session, header=header)


if __name__ == "__main__":
    main()
