#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2022/7/27 21:30'
import re
import json
import requests
import platform
from pyquery import PyQuery as pq


if platform.system().lower() == 'windows':
    from util.db import fundMongo, fundPositionMongo
elif platform.system().lower() == 'linux':
    from db import fundMongo, fundPositionMongo

headers = {

}


def request(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '__utmz=156575163.1646459642.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); historystock=301092%7C*%7C300033%7C*%7C002312; __utma=156575163.1412699886.1646459642.1658410613.1658572090.7; log=; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1657445360,1658410610,1658572087,1658927557; Hm_lvt_a47da7b82bdb6445aef7aaa2b00470b0=1658572252,1658927567; Hm_lpvt_a47da7b82bdb6445aef7aaa2b00470b0=1658927567; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1658927705; v=A282j4IyUQd6AVU7S1dh21qJ_oh8FMOoXWnHKoH8Cb_ldIF2ieRThm04V2mS',
        'Referer': 'https://fund.10jqka.com.cn/006009/pubnote.html',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'envtag': 'yzg',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return None


def get_fund_list():
    url = 'https://fund.10jqka.com.cn/hqcode.js'
    text = request(url)
    result = json.loads(text.replace('var hqjson=', ''))
    return result.keys()


def get_fund_position():
    codes = get_fund_list()
    for code in list(codes)[13000:]:
        url = 'https://fund.10jqka.com.cn/{code}/portfolioindex.html'.format(code=code)
        html = request(url)
        get_fund_position_parse(html)


def get_fund_position_parse(html):
    if not html:
        return
    doc = pq(html)
    fund = {}
    positions = []
    stocks = doc('#zcgList>.s-list>.data').items()
    for stock in stocks:
        item = {}
        item['index'] = stock('ul>li:nth-child(1)').text()
        item['name'] = stock('ul>li:nth-child(2)>a').text()
        if not item['name']:
            item['name'] = stock('ul>li:nth-child(2)').text()
        item['hold'] = stock('ul>li:nth-child(3)').text()
        item['market_value'] = stock('ul>li:nth-child(4)').text()
        item['proportion'] = stock('ul>li:nth-child(5)').text()
        positions.append(item)
    fund['name'] = re.search("fundCode = '(.+?)'", html).group(1)
    fund['code'] = re.search("fundName = '(.+?)'", html).group(1)
    fund['tabs'] = re.search("fundType = '(.+?)'", html).group(1)
    fund['positions'] = positions
    print(fund)
    fundMongo.insert_one(fund)


def fundPosition():
    funds = fundMongo.find({})
    positions = []
    for fund in funds:
        names = [item['name'] for item in positions]
        for position in positions:
            if position['name'] in names:
                index = names.index(position['name'])
                positions[index]['proportion'] += float(position['proportion'].replace('%', ''))
                positions[index]['funds'].append(fund['name'])
                positions[index]['codes'].append(fund['code'])
            else:
                proportion = float(position['proportion'].replace('%', ''))
                item = {'name': position['name'], 'proportion': proportion, 'funds': [fund['name']], 'codes': [fund['code']]}
                positions.append(item)
        print(positions)




if __name__ == '__main__':
    get_fund_position()
    # fundPosition()