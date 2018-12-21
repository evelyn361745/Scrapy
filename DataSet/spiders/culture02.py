# coding:utf-8


import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import CultureItem
import time

count = 1749
class Culture02Spider(scrapy.spiders.Spider):
    name = "culture02"
    start_urls = ["http://channel.chinanews.com/cns/cl/cul-gjqt.shtml?pager=0", ]
    for i in range(1, 187):
        url = start_urls[0][:-1] + str(i)
        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        # /html/body/div[3]/div[2]/table[1]/tbody/tr[1]/td[1]/a/html/body/div[3]/div[2]/table[3]/tbody/tr[1]/td[1]/a

        links = selector.xpath('/html/body/div[3]/div[2]/table/tr[1]/td[1]/a/@href').extract()
        print links
        titles = selector.xpath('/html/body/div[3]/div[2]/table/tr[1]/td[1]/a/text()').extract()
        for i in range(len(links)):
            link = links[i].strip()
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
        #//*[@id="cont_1_1_2"]/div[5]/p[2]
        content = sel.xpath('//*[@id="cont_1_1_2"]/div/p/text()').extract()
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            count = count + 1
            item['No'] = count
            return item
