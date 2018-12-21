# coding:utf-8


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import SciItem
import time

count = 0
class Sci01Spider(scrapy.spiders.Spider):
    name = "sci01"
    #https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2515
    # &k=&num=50&page=2&r=0.6684880747220743&callback=
    # jQuery31108580622671891815_1541999318184&_=1541999318215
    s = "https://news.sina.com.cn/roll/#pageid=153&lid=2515&k=&num=50&page="
    #m = ".shtml"
    start_urls = ["https://news.sina.com.cn/roll/#pageid=153&lid=2515&k=&num=50&page=1", ]
    for i in range(2, 1740):
        url = s+str(i)
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        #//*[@id="d_list"]/ul[9]/li[1]/span[2]/a
        links = selector.xpath('//*[@id="d_list"]/ul/li/a/@href').extract()
        print links
        titles = selector.xpath('//*[@id="d_list"]/ul/li/a/text()').extract()
        for i in range(len(links)):
            #
            link = links[i].strip()
            print link
            title = titles[i]
            yield Request(link.encode('utf-8'), meta={'title': title, 'link': link},
                          callback=self.parse_content)  # parse content

    def parse_content(self, response):
        global count
        item = SciItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        #print "in parse_content"
        sel = Selector(response)
        #//*[@id="artibody"]/p[1]
        #//*[@id="artibody"]/p[9]
        content = sel.xpath('//*[@id="artibody"]/p/text()').extract()
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            count = count + 1
            item['No'] = count
            print count
            return item
