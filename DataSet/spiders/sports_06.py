#coding:utf-8
#@author:hya

import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from DataSet.items import SportsItem
import time

class Sports6Spider(scrapy.spiders.Spider):
    name = "sports_06"
    #start_urls = ["http://sports.qq.com/l/csocce/newgz/zgnews/list20110822223448_2.htm",]
    #start_urls = ["http://sports.qq.com/l/others/paiq/list201203611739_2.htm",]
    #start_urls = ["http://sports.qq.com/l/others/newsroll_2.htm",]
    #start_urls = ["http://fiba.qq.com/l/fibawc/wcxinwen/list2017055171252_2.htm",]
    #start_urls = ["http://sports.qq.com/l/others/swimin/dyynews/roll_2.htm",]
    start_urls = ["http://sports.qq.com/l/others/run/runnews/roll_2.htm",]
    for i in range(3,50):
        url = start_urls[0][:47]+ str(i)+".htm"
        start_urls.append(url)

#    url = "http://sports.sohu.com/1/0304/51/subject219295140_342.shtml"
#    for i in range(244,342):
#        url = url[:-9]+ str(i)+".shtml"
#        start_urls.append(url)

#    url = "http://sports.sohu.com/1/0903/33/subject213643307_184.shtml"
#    for i in range(86,185):
#        url = url[:50]+ str(i)+".shtml"
#        start_urls.append(url)
#    url = "http://sports.sohu.com/s2008/2884/s259723255/index_1.shtml"
#    for i in range(1, 87):
#        url = url[:51]+ str(i)+".shtml"
#        start_urls.append(url)
#    url = "http://sports.sohu.com/s2005/volleyballnews_196.shtml"
#    for i in range(98, 197):
#        url = url[:44]+ str(i)+".shtml"
#        start_urls.append(url)
#    url = "http://sports.sohu.com/s2005/pingpangqiudongtai_764.shtml"
#    for i in range(666, 765):
#        url = url[:48]+ str(i)+".shtml"
#        print url
#        start_urls.append(url)
#    url = "http://sports.sohu.com/s2005/3275/s224453275_607.shtml"
#    for i in range(607, 706):
#        url = url[:-9]+ str(i)+".shtml"
#        print url
#        start_urls.append(url)

    def parse(self, response):
        selector = Selector(response)
        links = selector.xpath('/html/body/div[4]/div[3]/div[1]/ul/li/a/@href').extract()
        print links 
        titles = selector.xpath('/html/body/div[4]/div[3]/div[1]/ul/li/a/text()').extract()
        for i in range(len(links)):
            link = links[i]
            print link
            title = titles[i]
            yield Request(link.encode('utf-8'),meta={'title':title,'link':link},callback=self.parse_content) # parse content
        
#        for i in range(244,342):
#            url = response.url[:-9]+ str(i)+".shtml"
#            print url
#            yield Request(url, callback=self.parse)

    def parse_content(self, response):
        item = SportsItem()
        item["link"] = response.meta['link']
        item["title"] = response.meta['title']
        print "in parse_content"
        sel = Selector(response)
        content = sel.xpath('//*[@id="Cnt-Main-Article-QQ"]/p/text()').extract()
        if len(content) == 0:
            pass
        else:
            tmp = ''.join(content)
            item['content'] = tmp
            return item
