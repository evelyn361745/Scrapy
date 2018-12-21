# coding:utf-8


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import CultureItem
import time

count = 20019
class Culture04Spider(scrapy.spiders.Spider):
    name = "culture04"
    s = "http://www.offcn.com/shizheng/szrd/wenhua/"
    m = ".html"
    start_urls = ["http://www.offcn.com/shizheng/szrd/wenhua/"]
    for i in range(2,427):
        url = s + str(i)+m
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        #/html/body/div/div/div/ul[2]/li[1]/p/a
        #/html/body/div/div/div/ul[3]/li[4]/p/a
        links = selector.xpath('//*[@class="zg_main_left"]/dl/dt/a/@href').extract()
        print links
        titles = selector.xpath('//*[@class="zg_main_left"]/dl/dt/a/text()').extract()
        for i in range(len(links)):
            #http://www.cwhweb.com/news.php?id=223
            link =links[i].strip()
            print link
            title = titles[i]
            yield Request(link.encode('utf-8'), meta={'title': title, 'link': link},
                          callback=self.parse_content)  # parse content

    def parse_content(self, response):
        global count
        item = CultureItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        print "in parse_content"
        sel = Selector(response)
        #/html/body/div[4]/div[1]/div[2]/p[1]/text()
        #/html/body/div[4]/div[1]/div[2]/p[2]
        content = sel.xpath('/html/body/div[4]/div[1]/div[2]/p/text()').extract()
        if len(content) == 0:
            tmp = ''.join(content)
            item['content'] = tmp
            count = count + 1
            item['No'] = count
            return item
