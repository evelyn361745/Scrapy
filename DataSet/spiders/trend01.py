# coding:utf-8


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import TrendItem
import time

count = 38123
class Trend01Spider(scrapy.spiders.Spider):
    name = "trend01"
    #http://roll.mil.news.sina.com.cn/col/gjjq/index.shtml
    s = "http://www.zgss01.com/e/d/list_4_"
    m = ".html"
    start_urls = ["http://www.zgss01.com/e/d/list_4_1.html", ]
    for i in range(2, 1220):
        url = s+str(i)+m
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        #/html/body/div[5]/div/div/div[1]/div[2]/div[9]/div[1]/h2/a/b
        links = selector.xpath('//*[@class="lml_top"]/h2/a/@href').extract()
        print links
        titles = selector.xpath('//*[@class="lml_top"]/h2/a/text()').extract()
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
        #//*[@id="neirong_box"]/p[2]
        content = sel.xpath('//*[@id="neirong_box"]/p/text()').extract()
        if len(content) != 0:
            tmp = ''.join(content)
            item['content'] = tmp
            count = count + 1
            item['No'] = count
            print count
            return item
