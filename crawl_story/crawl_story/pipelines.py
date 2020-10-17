# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlite3 import dbapi2 as sqlite

class CrawlStoryPipeline:
    def __int__(self):
        self.connection = sqlite.connect('story.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Story(
            name_chap TEXT,
            content TEXT
        )''')

    def process_item(self, item, spider):
        return item
