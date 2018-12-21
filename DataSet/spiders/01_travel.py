#coding:utf-8
#@author:hya

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

class TravelSpider(scrapy.spiders.Spider):
    name = "travel"
    allowed_domains = ["travel.china.com"]
    start_urls = ["https://travel.china.com/hotspot/index_1.html"]

    def parse(self, response):
        selector = Selector(response)
        #link = selector.xpath("div[@class='listnewsarea']/div[@class='m_Con']/div[2]/h2/a/@href")
        link = selector.xpath('div[@class="listnewsarea"]')
        title = selector.xpath("div[@class='listnewsarea']/div[@class='m_Con']/div[2]/h2/a/text()")
        print link, title
