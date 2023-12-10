from bs4 import BeautifulSoup
from task3.parsers.extend_parser.dataclasses import SetItems


class ExtendParser:
    BASE_URL = "https://chrome.google.com/webstore/sitemap"

    def parse_sitemap(self, response_text: str):
        soup = BeautifulSoup(response_text, 'lxml')
        for url in soup.select('sitemap'):
            yield url.loc.text

    def parse_webstore_sitemap(self, response_text: str):
        soup = BeautifulSoup(response_text, 'lxml')
        for url in soup.select("url"):
            yield url.loc.text

    def parse_webstore_(self, response_text: str):
        soup = BeautifulSoup(response_text, 'lxml')
        #Take Name
        section = soup.select_one("section.lwrbTd")
        div = section.select_one("div.dSsD7e")
        a = div.select_one("a.KgGEHd")
        name = a.select_one("h1.Pa2dE").text
        #Take Info
        section = soup.select_one("section.H8vIqf")
        info = section.select_one("div.uORbKe").text.replace("\n", "")
        return SetItems(
            name=name,
            info=info
        )
