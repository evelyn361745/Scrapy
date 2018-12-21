# coding:utf-8


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import TrendItem
import time

count = 0
class Trend01Spider(scrapy.spiders.Spider):
    name = "trend01"
    #http://roll.mil.news.sina.com.cn/col/gjjq/index.shtml
    s = "http://roll.fashion.sina.com.cn/style/trend/index"
    m = ".shtml"
    start_urls = ["http://roll.fashion.sina.com.cn/style/trend/index_1.shtml", ]
    for i in range(1, 498):
        url = s+"_"+str(i)+m
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        #/html/body/div[1]/div[5]/div[1]/div[2]/div[10]/h2/a
        links = selector.xpath('//*[@class="blk_01"]/div/h2/a/@href').extract()
        print links
        titles = selector.xpath('//*[@class="blk_01"]/div/h2/a/text()').extract()
        for i in range(len(links)):
            #
            link = links[i].strip()
            print link
            title = titles[i]
            yield Request(link.encode('utf-8'), meta={'title': title, 'link': link},
                          callback=self.parse_content)  # parse content

    def parse_content(self, response):
        global count
        item = TrendItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        #print "in parse_content"
        sel = Selector(response)
        #//*[@id="article"]/p[3]
        #//*[@id="artibody"]/p[2]
        content = sel.xpath('//*[@id="article"]/p/text()').extract()
        if len(content) == 0:
            content = sel.xpath('//*[@id="artibody"]/p/text()').extract()
        tmp = ''.join(content)
        item['content'] = tmp
        count = count + 1
        item['No'] = count
        print count
        return item
