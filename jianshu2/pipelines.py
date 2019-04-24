# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class Jianshu2Pipeline(object):

    def __init__(self):
        conn = pymysql.connect(host='localhost',user='root',passwd='root',db='jianshu1',port=3306,charset='utf8')
        cursor = conn.cursor()
        self.post = cursor


    def process_item(self, item, spider):
        cursor = self.post
        #cursor.execute("use jianshu1")
        sql = "insert into jianshu(yonghu,shijian,title,yueduliang,comment,xihuan,gain) values('{}','{}','{}','{}','{}','{}','{}')".format(item['user'],item['time'],item['title'],item['view'],item['comment'],item['like'],item['gain'])
        cursor.execute(sql)
        cursor.connection.commit()
        return item
