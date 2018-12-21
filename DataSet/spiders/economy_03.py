#coding:utf-8
#@author:hya

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import EconomyItem
import time

class Economy3Spider(scrapy.spiders.Spider):
    name = "economy_03"
    #allowed_domains = ["finance.eastomoney.com"]
    start_urls = ["http://finance.eastmoney.com/news/cgnjj_1.html",
            "http://finance.eastmoney.com/a/czqyw_1.html",
            "http://finance.eastmoney.com/news/cgspl_1.html",
            ]
    
    for i in range(2,26):
    #    url = start_urls[0][:41]+str(i)+".html"
    #    print url
    #    start_urls.append(url)
    #    url = start_urls[1][:36]+str(i)+".html"
    #    print url
    #    start_urls.append(url)

        url = start_urls[2][:39]+str(i)+".html"
        print url
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        print response.url
        links = selector.xpath('//*[@id="newsListContent"]/li/div/p[1]/a/@href').extract()
        titles = selector.xpath('//*[@id="newsListContent"]/li/div/p[1]/a/text()').extract()
        #print links,titles 
        for i in range(len(links)):
            link = links[i]
            link = links[i]
            title = titles[i]
            print link,title
            yield Request(link.encode('utf-8'),meta={'title':title,'link':link},callback=self.parse_content) # parse content


    def parse_content(self, response):
        item = EconomyItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        print "in parse_content"
        sel = Selector(response)
        content = sel.xpath('//*[@id="ContentBody"]/p/text()').extract()
        print content   
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            return item
