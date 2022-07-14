import json,re
from django.views.generic.base import View
from django.shortcuts import HttpResponse
from util.db import codeMongo
from util.params import WENCAI_HEADERS
import requests, time


class LimitUp(View):

    def get(self, request):
        url = 'http://ai.iwencai.com/urp/v7/landing/getDataList'
        payload = 'query=%E6%98%A8%E6%97%A5%E6%B6%A8%E5%81%9C&urp_sort_way=desc&page=1&perpage=50&condition=%5B%7B%22dateText%22%3A%22%E6%98%A8%E6%97%A5%22%2C%22indexName%22%3A%22%E6%B6%A8%E5%81%9C%22%2C%22indexProperties%22%3A%5B%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020220708%22%5D%2C%22dateUnit%22%3A%22%E6%97%A5%22%2C%22source%22%3A%22new_parser%22%2C%22type%22%3A%22index%22%2C%22indexPropertiesMap%22%3A%7B%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220220708%22%7D%2C%22reportType%22%3A%22TRADE_DAILY%22%2C%22dateType%22%3A%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%2C%22chunkedResult%22%3A%22%E6%98%A8%E6%97%A5%E6%B6%A8%E5%81%9C%22%2C%22valueType%22%3A%22_%E6%98%AF%E5%90%A6%22%2C%22domain%22%3A%22abs_%E8%82%A1%E7%A5%A8%E9%A2%86%E5%9F%9F%22%2C%22uiText%22%3A%22%E6%98%A8%E6%97%A5%E7%9A%84%E6%B6%A8%E5%81%9C%22%2C%22sonSize%22%3A0%2C%22queryText%22%3A%22%E6%98%A8%E6%97%A5%E7%9A%84%E6%B6%A8%E5%81%9C%22%2C%22relatedSize%22%3A0%2C%22tag%22%3A%22%5B%E6%98%A8%E6%97%A5%5D%E6%B6%A8%E5%81%9C%22%7D%5D&comp_id=6257151&business_cat=soniu&uuid=24087'
        response = requests.request("POST", url, headers=WENCAI_HEADERS, data=payload)
        limitUpList = json.loads(response.text)['answer']['components'][0]['data']['datas']
        date = time.strftime('%Y%m%d', time.localtime(int(time.time())))
        print('date: ', date)
        limitUps = [{
            'code': item['code'],
            'name': item['股票简称'],
            'many': item['连续涨停天数[%s]'%date],
            'days': item['几天几板[%s]'%date],
            'type': item['涨停类型[%s]'%date],
            'cause': item['涨停原因类别[%s]'%date],
            'price': item['最新价']
        } for item in limitUpList]
        return HttpResponse(json.dump(limitUps))

