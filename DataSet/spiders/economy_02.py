#coding:utf-8
#@author:hya

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import EconomyItem
import time

class Economy2Spider(scrapy.spiders.Spider):
    name = "economy_02"
    allowed_domains = ["www.xinjr.com"]
    start_urls = ["http://www.xinjr.com/caijing/renwu/index_2.html",
            ]
    
#    for i in range(3,1264):
#        url = start_urls[0][:41]+str(i)+".html"
#        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        links = selector.xpath('/html/body/div[6]/div[1]/div/ul/li/a/@href').extract()
        titles = selector.xpath('/html/body/div[6]/div[1]/div/ul/li/a/text()').extract()
        for i in range(len(links)):
            link = links[i]
            link = "http://www.xinjr.com"+ links[i]
            title = titles[i]
            print link,title
            yield Request(link.encode('utf-8'),meta={'title':title,'link':link, 'PhantomJS':True},callback=self.parse_content) # parse content


    def parse_content(self, response):
        item = EconomyItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        print "in parse_content"
        sel = Selector(response)
        content = sel.xpath('/html/body/div[7]/div[1]/div/div[2]/img[1]').extract()
        print content   
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            return item
