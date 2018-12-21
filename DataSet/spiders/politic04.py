# coding:utf-8


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import PoliItem
import time

count = 21831
class Politic04Spider(scrapy.spiders.Spider):
    name = "politic04"
    start_urls = ["http://sousuo.gov.cn/column/31421/0.htm", ]
    for i in range(1, 818):
        url = start_urls[0][:-1] + str(i)
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        #/html/body/div[2]/div/div[2]/div[2]/ul/li[1]/h4/a
        #/html/body/div[2]/div/div[2]/div[2]/ul/li[14]/h4/a
        #// *[ @ id = "UCAP-CONTENT"] / p[4] / text()
        links = selector.xpath('/html/body/div[2]/div/div[2]/div[2]/ul/li/h4/a/@href').extract()
        print links
        titles = selector.xpath('/html/body/div[2]/div/div[2]/div[2]/ul/li/h4/a/text()').extract()
        for i in range(len(links)):
            link = links[i].strip()
            print link
            title = titles[i]
            yield Request(link.encode('utf-8'), meta={'title': title, 'link': link},
                          callback=self.parse_content)  # parse content

    def parse_content(self, response):
        global count
        item = PoliItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        print "in parse_content"
        sel = Selector(response)
        #//*[@id="UCAP-CONTENT"]/p[2]
        content = sel.xpath('//*[@id="UCAP-CONTENT"]/p/text()').extract()
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            count = count + 1
            item['No'] = count
            return item
