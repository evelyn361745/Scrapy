# coding:utf-8

import re
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import YuleItem
import time

count = 0
class YuleSpider(scrapy.spiders.Spider):
    name = "yule"
    #http://roll.mil.news.sina.com.cn/col/gjjq/index.shtml
    #http://www.diyiyou.com/news/gnxw/index_2863.html
    s = "http://news.guilinlife.com/ent/"
    m = ".shtml"
    start_urls = ["http://news.guilinlife.com/ent/index.shtml", ]
    for i in range(2, 210):
        url = s+str(i)+m
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        #/html/body/div[2]/div/div[1]/ul/li[1]/div[1]/a
        links = selector.xpath('//*[@class="newLi"]/li/a/@href').extract()
        print links
        titles = selector.xpath('//*[@class="newLi"]/li/a/text()').extract()
        for i in range(len(links)):
            #h = "https://www.app178.com"
            link = links[i].strip()
            print link
            title = titles[i]
            yield Request(link.encode('utf-8'), meta={'title': title, 'link': link},
                          callback=self.parse_content)  # parse content

    def parse_content(self, response):
        global count
        item = YuleItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        #print "in parse_content"
        sel = Selector(response)
        #/html/body/div[7]/div/div/em/em/div[1]/p[6]/text()/html/body/div[7]/div/div/em/em/div[1]/p[6]/text()
        content = sel.xpath('//*[@id="content"]/p/text()').extract()
        #content = content.strip()
        #content = content.replace(" ","")
        if len(content) != 0:
            tmp = ''.join(content)
            item['content'] = tmp
            count = count + 1
            item['No'] = count
            print count
            return item
