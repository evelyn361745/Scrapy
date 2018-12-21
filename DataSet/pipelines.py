# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from items import SportsItem,EconomyItem,PoliItem,CultureItem,EduItem,ArmyItem,SciItem,TrendItem,GameItem,YuleItem


class DatasetPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, SportsItem):
            with open('/home/hya/DataSet/sports.txt', 'a') as fp:
                fp.write(item['title'].encode('utf-8')+'\n'+item['link'].encode('utf-8')+'\n'+item['content'].encode('utf-8')+'\n\n')
            return item
        elif isinstance(item, EconomyItem):
            with open('/home/hya/DataSet/economy.txt', 'a') as fp:
                fp.write(item['title'].encode('utf-8')+'\n'+item['link'].encode('utf-8')+'\n'+item['content'].encode('utf-8')+'\n\n')
            return item
        elif isinstance(item, PoliItem):
            with open('D:/poli.txt', 'a') as fp:
                fp.write(str(item['No'])+'\n'+item['title'].encode('utf-8')+'\n'+item['link'].encode('utf-8')+'\n'+item['content'].encode('utf-8')+'\n\n')
        elif isinstance(item, CultureItem):
            with open('D:/poli.txt', 'a') as fp:
                fp.write(str(item['No'])+'\n'+item['title'].encode('utf-8')+'\n'+item['link'].encode('utf-8')+'\n'+item['content'].encode('utf-8')+'\n\n')
        elif isinstance(item, EduItem):
            with open('D:/edu.txt', 'a') as fp:
                fp.write(str(item['No'])+'\n'+item['title'].encode('utf-8')+'\n'+item['link'].encode('utf-8')+'\n'+item['content'].encode('utf-8')+'\n\n')
        elif isinstance(item, ArmyItem):
            with open('D:/army.txt', 'a') as fp:
                fp.write(str(item['No'])+'\n'+item['title'].encode('utf-8')+'\n'+item['link'].encode('utf-8')+'\n'+item['content'].encode('utf-8')+'\n\n')
        elif isinstance(item, SciItem):
            with open('D:/sci.txt', 'a') as fp:
                fp.write(str(item['No']) + '\n' + item['title'].encode('utf-8') + '\n' + item['link'].encode('utf-8') + '\n' + item['content'].encode('utf-8') + '\n\n')
        elif isinstance(item, TrendItem):
            with open('D:/trend.txt', 'a') as fp:
                fp.write(str(item['No']) + '\n' + item['title'].encode('utf-8') + '\n' + item['link'].encode('utf-8') + '\n' + item['content'].encode('utf-8') + '\n\n')
        elif isinstance(item, GameItem):
            with open('D:/Data/dataset/game.txt', 'a') as fp:
                fp.write(str(item['No']) + '\n' + item['title'].encode('utf-8') + '\n' + item['link'].encode('utf-8') + '\n' + item['content'].encode('utf-8') + '\n\n')
        elif isinstance(item, YuleItem):
            with open('D:/Data/dataset/yule.txt', 'a') as fp:
                fp.write(str(item['No']) + '\n' + item['title'].encode('utf-8') + '\n' + item['link'].encode('utf-8') + '\n' + item['content'].encode('utf-8') + '\n\n')
