# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlStoryItem(scrapy.Item):
    # define the fields for your item here like:
    name_chap = scrapy.Field()
    content = scrapy.Field()
