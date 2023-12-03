# 3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи: цитата, автор, інфа про автора тощо. 
# - збирається інформація з 10 сторінок сайту.
# - зберігати зібрані дані у CSV файл
import requests
import csv
from bs4 import BeautifulSoup
import os


current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)


def write_csv_author_info(file_name,data):
    if os.path.exists(file_name):
        with open(file_name, 'a+', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Title', 'Born', 'Description'])
            writer.writerow(data)

    else:
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Title', 'Born', 'Description'])
            writer.writeheader()
            writer.writerow(data)


def write_csv_based_page(file_name,data):
    if os.path.exists(file_name):
        with open(file_name, 'a+', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Text', 'Author', 'Tags'])
            for item in data['data']:
               writer.writerow(item)

    else:
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Text', 'Author', 'Tags'])
            writer.writeheader()
            for item in data['data']:
                writer.writerow(item)


def take_authors(pages = 10):
    authors = []
    authors_links = []
    for page in range(1,pages+1):
        url = f"http://quotes.toscrape.com/page/{page}/"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            for block in soup.select("div.quote"):
                author = block.select("span")[-1].select_one('a')["href"]
                if author.split('/')[-1] not in authors:
                    authors.append(author.split('/')[-1])
                    authors_links.append({"Author":author.split('/')[-1], "Link":author})

    return authors_links
        

def take_info_about_authors(data):
    for author in data:
        url = f"http://quotes.toscrape.com{author['Link']}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            title = soup.select_one("h3.author-title").text
            born_date = soup.select_one("span.author-born-date").text
            born_location = soup.select_one("span.author-born-location").text
            description = (soup.select_one("div.author-description").text).lstrip()
            write_csv_author_info(os.path.join(parent_directory, 'author_info.csv'),{"Title":title, "Born" : born_date +" "+ born_location,"Description":repr(description)})


def pars_page(page=1):
    data = {"page" : page,"data" : []}
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        find_block = soup.select("div.quote")
        data_blocks = []
        for block in find_block:
            #Основний тектс
            span_based_text = block.select_one("span.text").text.replace('“','"').replace('”','"')
            #Автор
            span_author = block.select_one("small.author").text
            div_tags = block.select_one("div.tags")
            #Список тегів
            tags = [i.text for i in div_tags.select('a')]
            data_blocks.append({"Text": span_based_text, "Author" : span_author, "Tags" : ','.join(tags)})
        data["data"] = data_blocks
        write_csv_based_page(os.path.join(parent_directory, 'output.csv'),data)
    else:
        print("Something wrong")


def main():
    for page in range(1,11):
        pars_page(page)
    take_info_about_authors(take_authors())


if __name__ == "__main__":
    main()