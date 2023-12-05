# 3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи: цитата, автор, інфа про автора тощо. 
# - збирається інформація з 10 сторінок сайту.
# - зберігати зібрані дані у CSV файл
import requests
import csv
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)


def write_in_csv_file(data):
    with open(os.path.join(parent_directory, 'output.csv'), 'a+', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Quote', 'Authors', 'Tags','Description'])
        writer.writeheader()
        for item in data:
           writer.writerow(item)




def take_description_pages(url,):
    start_url = "http://quotes.toscrape.com"
    response = requests.get(urljoin(start_url,url))
    if response.status_code == 200:
        return response.content


def pars_description_pages(response):
    soup = BeautifulSoup(response, 'lxml')
    born_date = soup.select_one("span.author-born-date").text
    born_location = soup.select_one("span.author-born-location").text
    description = (soup.select_one("div.author-description").text).lstrip()
    return born_date + " " + born_location + repr(description)


def pars_pages(response,data = []):
    data_authors = {"Link" : [], "Description" : []}
    soup = BeautifulSoup(response.content, 'lxml')
    div_blocks = soup.select("div.quote")
    for div_block in div_blocks:
        quote = div_block.select_one("span.text").text.replace('“','"').replace('”','"')
        authors = div_block.select_one("small.author").text
        authors_link = div_block.select_one("span:not([class]) a")["href"]
        tags = [_.text for _ in div_block.select("a.tag")]
        if authors_link not in data_authors["Link"]:
            data_authors["Link"].append(authors_link)
            data_authors["Description"].append(pars_description_pages(take_description_pages(authors_link)))
        description = data_authors["Description"][data_authors["Link"].index(authors_link)]

        data.append({"Quote": quote,"Authors": authors,"Tags": tags,"Description" : description})
    
    next_page = soup.select_one("li.next a")
    if next_page:
        return next_page["href"],data
    else:
        return None,data



def take_based_pages(url = None,page = 1,data = None):
    if url is None:
        url = "http://quotes.toscrape.com/"
    if page != 11:
        response = requests.get(url)
        if response.status_code == 200:
            page_link,data = pars_pages(response)
            next_page = urljoin("http://quotes.toscrape.com/",page_link)
            print(page,url)
            take_based_pages(url = next_page,page=page+1,data = data)
    else:
        write_in_csv_file(data)

take_based_pages()
        
