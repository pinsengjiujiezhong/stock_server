#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2022/7/7 21:11'
import pymongo
import platform

# if platform.system().lower() == 'windows':
#     client = pymongo.MongoClient()
# elif platform.system().lower() == 'linux':
#     client = pymongo.MongoClient('49.232.3.50:37017')
client = pymongo.MongoClient('49.232.3.50:37017')
mydb = client.stock
roseMongo = mydb.rose
codeMongo = mydb.code
dateLineMongo = mydb.dateline