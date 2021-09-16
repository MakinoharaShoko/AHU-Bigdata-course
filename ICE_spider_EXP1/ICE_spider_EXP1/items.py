# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    nickname = scrapy.Field()
    like = scrapy.Field()
    fans = scrapy.Field()
    prestige = scrapy.Field()
    location = scrapy.Field()