#coding:utf-8
#@author:hya

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import SportsItem
import time

class Sports5Spider(scrapy.spiders.Spider):
    name = "sports_05"
    start_urls = ["http://channel.chinanews.com/cns/cl/ty-gnzq.shtml?pager=1",]
    for i in range(2,1000):
        url = start_urls[0][:-1]+ str(i)
        start_urls.append(url)


    def parse(self, response):
        selector = Selector(response)
        #/html/body/div[3]/div[2]/table[1]/tbody/tr[1]/td[1]/a
        #//*[@id="cont_1_1_2"]/h1
        #//*[@id="cont_1_1_2"]/div[6]/p[1]
        #/html/body/div[3]/div[2]/table[3]/tbody/tr[1]/td[1]/a
        links = selector.xpath('/html/body/div[3]/div[2]/table/tr[1]/td[1]/a/@href').extract()
        print links 
        titles = selector.xpath('/html/body/div[3]/div[2]/table/tr[1]/td[1]/a/text()').extract()
        for i in range(len(links)):
            link = links[i].strip()
            print link
            title = titles[i]
            yield Request(link.encode('utf-8'),meta={'title':title,'link':link},callback=self.parse_content) # parse content
        

    def parse_content(self, response):
        item = SportsItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        print "in parse_content"
        sel = Selector(response)
        content = sel.xpath('///*[@id="cont_1_1_2"]/div[6]/p/text()').extract()
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            return item
