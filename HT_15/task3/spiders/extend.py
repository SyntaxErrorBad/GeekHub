import scrapy
from scrapy.http import Response
from scrapy import Request

from typing import Any

from task3.parsers.extend_parser.parser import ExtendParser
from task3.items import Task3Item


class ExtendSpider(scrapy.Spider):
    parser = ExtendParser()
    name = "extend"
    start_urls = [parser.BASE_URL]

    def parse(self, response: Response, **kwargs: Any):
        results = self.parser.parse_sitemap(response.text)
        for result in results:
            yield Request(
                url=result,
                callback=self.parse_sitemap,
            )
    
    def parse_sitemap(self, response: Response):
        results = self.parser.parse_webstore_sitemap(response.text)
        for result in results:
            yield Request(
                url=result,
                callback=self.parse_webstore,
            )

    def parse_webstore(self, response: Response):
        result = self.parser.parse_webstore_(response.text)
        item = Task3Item()
        item["name"] = result.name
        item["info"] = result.info
        yield item
