#coding=utf-8
import json
import pymysql
from django.views.generic.base import View
from django.shortcuts import render, HttpResponse
from util.db import roseMongo

def executeSql(sql):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='stock',
                         charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchall()
    return data


class Rose(View):
    def get(self, request):
        size = int(request.GET.get('size', ''))
        page = int(request.GET.get('page', ''))
        keyword = request.GET.get('keyword', '')
        searchItem = {}
        if keyword:
            searchItem = {'name': {'$regex': keyword}}
        mongoC = roseMongo.find(searchItem)
        total = mongoC.count()
        roseList = mongoC.limit(size).skip((page-1)*size).sort('num', -1)
        roses = []
        for rose in roseList:
            del rose['_id']
            roses.append(rose)
        result = {
            'roses': roses,
            'total': total
        }
        return HttpResponse(json.dumps(result))

