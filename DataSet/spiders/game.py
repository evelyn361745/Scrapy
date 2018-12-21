# coding:utf-8

import re
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import GameItem
import time

count = 0
class GameSpider(scrapy.spiders.Spider):
    name = "game"
    #http://roll.mil.news.sina.com.cn/col/gjjq/index.shtml
    #http://www.diyiyou.com/news/gnxw/index_2863.html
    s = "https://www.app178.com/xinwen_"
    m = ".html"
    start_urls = ["https://www.app178.com/xinwen_1.html", ]
    for i in range(2, 1386):
        url = s+str(i)+m
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        #/html/body/div[2]/div/div[1]/ul/li[1]/div[1]/a
        links = selector.xpath('//*[@class="list_left"]/ul/li/div/a/@href').extract()
        print links
        titles = selector.xpath('//*[@class="list_left"]/ul/li/div/a/text()').extract()
        for i in range(len(links)):
            h = "https://www.app178.com"
            link = h + links[i].strip()
            print link
            title = titles[i]
            yield Request(link.encode('utf-8'), meta={'title': title, 'link': link},
                          callback=self.parse_content)  # parse content

    def parse_content(self, response):
        global count
        item = GameItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        #print "in parse_content"
        sel = Selector(response)
        #/html/body/div[7]/div/div/em/em/div[1]/p[6]/text()/html/body/div[7]/div/div/em/em/div[1]/p[6]/text()
        content = sel.xpath('//*[@class="jjzq_ny_left1_main"]/p/text()').extract()
        #content = content.strip()
        #content = content.replace(" ","")
        if len(content) != 0:
            tmp = ''.join(content)
            item['content'] = tmp
            count = count + 1
            item['No'] = count
            print count
            return item
