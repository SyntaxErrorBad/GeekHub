# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import os


current_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(current_file_path)


class Task3Pipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        with open(os.path.join(parent_directory, 'output.csv'), 'a+', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'info'])
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(adapter.asdict())
        #Якщо потрібен вивід в консоль
        #return item
