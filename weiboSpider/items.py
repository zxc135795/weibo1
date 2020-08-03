# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    id = scrapy.Field()
    shoucang = scrapy.Field()
    pinglun = scrapy.Field()
    zhuanfa = scrapy.Field()
    zan = scrapy.Field()
    key = scrapy.Field()
