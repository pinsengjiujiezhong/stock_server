#coding=utf-8
import json
import pymysql
from django.views.generic.base import View
from django.shortcuts import render, HttpResponse
from util.db import roseMongo, hardenMongo


class Rose(View):
    def get(self, request):
        size = int(request.GET.get('size', ''))
        page = int(request.GET.get('page', ''))
        keyword = request.GET.get('keyword', '')
        types = request.GET.get('types', 'num')
        order = request.GET.get('order', '')
        orderType = -1
        if order == 'ascending':
            orderType = 1
        searchItem = {}
        if keyword:
            searchItem = {'name': {'$regex': keyword}}
        mongoC = roseMongo.find(searchItem)
        total = mongoC.count()
        roseList = mongoC.limit(size).skip((page-1)*size).sort(types, orderType)
        roses = []
        for rose in roseList:
            del rose['_id']
            rose['price'] = rose['prices'][0]
            roses.append(rose)
        result = {
            'roses': roses,
            'total': total
        }
        return HttpResponse(json.dumps(result))


class Harden(View):
    def get(self, request):
        size = int(request.GET.get('size', ''))
        page = int(request.GET.get('page', ''))
        keyword = request.GET.get('keyword', '')
        order = request.GET.get('order', '')
        harden = request.GET.get('harden', '')
        orderType = -1
        if order == 'ascending':
            orderType = 1
        searchItem = {}
        if keyword:
            searchItem['name'] = {'$regex': keyword}
        if harden == 'true':
            searchItem['is_harden'] = True
        print(searchItem)
        mongoC = hardenMongo.find(searchItem)
        total = mongoC.count()
        hardenList = mongoC.limit(size).skip((page-1)*size).sort('monthharden', orderType)
        hardens = []
        for harden in hardenList:
            del harden['_id']
            harden['price'] = harden['prices'][0]
            hardens.append(harden)
        result = {
            'hardens': hardens,
            'total': total
        }
        return HttpResponse(json.dumps(result))

