# coding:utf-8


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import PoliItem
import time

count = 25760
class Politic05Spider(scrapy.spiders.Spider):
    name = "politic05"
    s = "http://www.offcn.com/shizheng/szrd/zhengzhi/"
    m = ".html"
    #http://news.qianlong.com/qlyc/qlsz1/index_1.shtml
    start_urls = ["http://www.offcn.com/shizheng/szrd/zhengzhi/", ]
    for i in range(2, 472):
        url = s + str(i)+m
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        #/html/body/div[4]/div[1]/dl[1]/dt/a
        links = selector.xpath('//*[@class="zg_main_left"]/dl/dt/a/@href').extract()
        print links
        titles = selector.xpath('//*[@class="zg_main_left"]/dl/dt/a/text()').extract()
        for i in range(len(links)):
            #http://news.youth.cn/sz/201811/t20181105_11774697.htm
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
        #//*[@id="Cnt-Main-Article-QQ"]/p[5]
        content = sel.xpath('//*[@class="zgsz_sContent clearfix"]/p/text()').extract()
        if len(content) != 0:
            tmp = ''.join(content)
            item['content'] = tmp
            count = count + 1
            item['No'] = count
            return item

