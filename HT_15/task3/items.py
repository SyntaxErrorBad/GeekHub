# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item
from scrapy.item import Field


class Task3Item(Item):
    name = Field()
    info = Field()
