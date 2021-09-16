# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from pymysql.cursors import Cursor

from ICE_spider_EXP1.items import UserItem

class IceSpiderExp1Pipeline(object):
    def __init__(self):
        self.connection = pymysql.connect(
            host = '192.168.195.134',
            port = 3306,
            user = 'kamome',
            password = '123456',
            db = 'ICE_spider_EXP1',
            charset='utf8mb4'
        )

    def process_item(self,item,spider):
        if isinstance(item,UserItem):
            cursor = self.connection.cursor()
            cursor.execute('insert into `users` (`username`,`nickname`,`like`,`fans`,`prestige`,`location`) values (%s,%s,%s,%s,%s,%s)',(item['username'],item['nickname'],item['like'],item['fans'],item['prestige'],item['location']))
            self.connection.commit()