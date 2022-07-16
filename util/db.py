#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2022/7/7 21:11'
import pymongo

# client = pymongo.MongoClient()
client = pymongo.MongoClient('49.232.3.50')
mydb = client.stock
roseMongo = mydb.rose
codeMongo = mydb.code
dateLineMongo = mydb.dateline