#coding:utf-8
#@author:hya

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import EconomyItem
import time

class SportsSpider(scrapy.spiders.Spider):
    name = "economy_01"
    allowed_domains = ["www.ceweekly.cn"]
    start_urls = ["http://www.ceweekly.cn/finance/banking/1.shtml",
            "http://www.ceweekly.cn/finance/bond/1.shtml",
            "http://www.ceweekly.cn/finance/macro/",
            "http://www.ceweekly.cn/finance/capital/1.shtml",]
    

    def parse(self, response):
        selector = Selector(response)
        links = selector.xpath('/html/body/div[3]/section/section/section/ul/li/a/@href').extract()
        titles = selector.xpath('/html/body/div[3]/section/section/section/ul/li/a/text()').extract()
        for i in range(len(links)):
            link = links[i]
            title = titles[i]
            yield Request(link.encode('utf-8'),meta={'title':title,'link':link},callback=self.parse_content) # parse content

        nextlink = selector.xpath('/html/body/div[3]/section/section/section/div/ul/li[9]/a/@href').extract()
        print nextlink
        if nextlink:
            url = nextlink[0]
            yield Request(url, callback=self.parse)

    def parse_content(self, response):
        item = EconomyItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        print "in parse_content"
        sel = Selector(response)
        content = sel.xpath('/html/body/section/section/article/div[1]/div[2]/p/text()').extract()
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            return item
