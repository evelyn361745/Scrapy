# coding:utf-8


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import EduItem
import time

count = 88775
class Edu01Spider(scrapy.spiders.Spider):
    name = "edu01"
    #http://roll.edu.sina.com.cn/lm/ky3/kyzx/kaoshi/index_555.shtml
    s = "http://roll.edu.sina.com.cn/all/sxy/index"
    m = ".shtml"
    start_urls = ["http://roll.edu.sina.com.cn/all/sxy/index_0.shtml", ]
    for i in range(1, 569):
        url = s+"_"+str(i)+m
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        #//*[@id="Main"]/div[3]/ul/li[1]/a
        links = selector.xpath('//*[@id="Main"]/div[3]/ul/li/a/@href').extract()
        print links
        titles = selector.xpath('//*[@id="Main"]/div[3]/ul/li/a/text()').extract()
        for i in range(len(links)):
            link = links[i].strip()
            print link
            title = titles[i]
            yield Request(link.encode('utf-8'), meta={'title': title, 'link': link},
                          callback=self.parse_content)  # parse content

    def parse_content(self, response):
        global count
        item = EduItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        #print "in parse_content"
        sel = Selector(response)
        #//*[@id="artibody"]/p[1]
        content = sel.xpath('//*[@id="artibody"]/p/text()').extract()
        #it = (sel.xpath('//*[@id="artibody"]'))
        #tmp = ""
        #for p in it.xpath('.//p/text()'):
           # tmp = tmp + p.extract().strip()
        #item['content'] = tmp
        #count = count + 1
        #item['No'] = count
        #return item
            # print count
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            count = count + 1
            item['No'] = count
            print count
            return item
