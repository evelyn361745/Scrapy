# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SportsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
    pass
class EconomyItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
    pass
class PoliItem(scrapy.Item):
    No = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
class CultureItem(scrapy.Item):
    No = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
class EduItem(scrapy.Item):
    No = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
class ArmyItem(scrapy.Item):
    No = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
class SciItem(scrapy.Item):
    No = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
class TrendItem(scrapy.Item):
    No = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
class GameItem(scrapy.Item):
    No = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
class YuleItem(scrapy.Item):
    No = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()