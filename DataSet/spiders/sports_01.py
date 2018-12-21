#coding:utf-8
#@author:hya

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import SportsItem
import time

class SportsSpider(scrapy.spiders.Spider):
    name = "sports_01"
    allowed_domains = ["sports.people.com.cn"]
    start_urls = ["http://sports.people.com.cn/GB/22134/index.html",
            "http://sports.people.com.cn/GB/22134/22139/index.html",
            "http://sports.people.com.cn/GB/22134/33285/index.html",
            "http://sports.people.com.cn/GB/22141/407506/index.html",
            "http://sports.people.com.cn/GB/22155/46613/index.html",
            "http://sports.people.com.cn/GB/22155/22157/48286/index.html",
            "http://sports.people.com.cn/GB/22149/index.html",
            "http://sports.people.com.cn/GB/22155/index.html",
            "http://sports.people.com.cn/GB/22141/index.html",]
    

    def parse(self, response):
        selector = Selector(response)
        links = selector.xpath('//*[@id="p2Ab_1"]/div/p/strong/a/@href').extract()
        titles = selector.xpath('//*[@id="p2Ab_1"]/div/p/strong/a/text()').extract()
        for i in range(len(links)):
            link = "http://sports.people.com.cn"+links[i]
            title = titles[i]
            yield Request(link.encode('utf-8'),meta={'title':title,'link':link},callback=self.parse_content) # parse content
        
        nextlink = selector.xpath('//*[@id="p2Ab_1"]/div[31]/a/@href').extract()
        for i in range(len(nextlink)):
            print response.url,nextlink[i]
            url = response.url[:-10]+nextlink[i]
            print url
            yield Request(url, callback=self.parse)

    def parse_content(self, response):
        item = SportsItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        print "in parse_content"
        sel = Selector(response)
        content = sel.xpath('//*[@id="rwb_zw"]/p/text()').extract()
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            return item
