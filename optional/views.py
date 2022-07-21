import json,re
from django.views.generic.base import View
from django.shortcuts import HttpResponse
from util.db import codeMongo
from util.params import GET_OPTIONAL_URL, TONGHUASHUN_HEADERS, GET_KLINE_URL
import requests


class Optional(View):

    def get(self, request):
        optionals = request.GET.get('optionals', '')
        url = GET_OPTIONAL_URL.format(code=optionals)
        print(url)
        response = requests.request("GET", url, headers=TONGHUASHUN_HEADERS, data={})
        optionals = json.loads(re.search('multimarketreal\((.+?)\)', response.text).group(1))
        optionalList = []
        for code in optionals['hs']:
            optional = optionals['hs'][code]
            item = {}
            item['code'] = code
            item['name'] = optional['name']
            item['transaction'] = optional['10']
            item['extent'] = optional['264648']
            item['percentage'] = optional['199112']
            item['opening'] = optional['7']
            item['change'] = optional['1968584']
            optionalList.append(item)
        return HttpResponse(json.dumps(optionalList))


class CheckCode(View):
    def get(self, request):
        code = request.GET.get('code', '')
        result = codeMongo.find_one({'symbol': code})
        check = False
        if result:
            check = True
        return HttpResponse(json.dumps({'check': check}))


class KLine(View):
    def get(self, request):
        code = request.GET.get('code', '')
        codeObj = codeMongo.find_one({'symbol': code})
        kcode = codeObj['ts_code'][-2:] + '_' + codeObj['symbol']
        url = GET_KLINE_URL.format(code=kcode)
        response = requests.request("GET", url, headers=TONGHUASHUN_HEADERS, data={})
        print('\"%s\":(.+?)\}\)'%kcode)
        KlineDict = json.loads(re.search('\"%s\":(.+?)\}\)'%kcode, response.text).group(1))
        kLineList = [item.split(',') for item in KlineDict['data'].split(';')]
        result = {
            'time': [item[0] for item in kLineList],
            'price': [item[1] for item in kLineList]
        }
        return HttpResponse(json.dumps(result))
