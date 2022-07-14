#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2022/7/8 21:56'

from util.db import codeMongo, dateLineMongo
import requests
import json, time

headers = {
  'Accept': 'application/json;charset=UTF-8',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json;charset=UTF-8',
  'Cookie': 'session-id=ec8e6942-becb-4921-a213-215a33555e36; uid=2|1:0|10:1657801528|3:uid|8:NTI2ODM3|dec1d63e25126568ac2186ee9d33ff782d4d992238ff4bbcf8fd7df45d49015a; username=2|1:0|10:1657801528|8:username|8:5p2o5Yev|3318c51b2c4f1d2b0d06c25b5336753d67de792fd652fc70443bfd45241921e9',
  'Origin': 'https://tushare.pro',
  'Referer': 'https://tushare.pro/webclient/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
  'envtag': 'yzg',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}


def request(url, data):
    for i in range(5):
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response.text
            break
        else:
            time.sleep(5)


def getStockNameInfo():
    data = {"user_id": 526837, "username": "杨凯", "user_valid": True, "root_id": "2", "doc_id": "25",
     "params": {"ts_code": "", "name": "", "exchange": "", "market": "", "is_hs": "", "list_status": "", "limit": "",
                "offset": ""}, "fields": ["name", "ts_code", "symbol", "market", "industry"]}
    url = 'https://tushare.pro/wctapi/apis/stock_basic'
    result = request(url, json.dumps(data))
    stockInfoList = json.loads(result)
    symbolList = [item['symbol'] for item in codeMongo.find()]
    for stock in stockInfoList['data']['items']:
        print(stock)
        if stock[1] in symbolList:
            continue
        item = {}
        item['ts_code'] = stock[0]
        item['symbol'] = stock[1]
        item['name'] = stock[2]
        item['industry'] = stock[3]
        item['market'] = stock[4]
        codeMongo.insert(item)



def getStockDateLine(ts_code, start_date, end_date):
    print('ts_code: ', ts_code)
    data = {"user_id":526837,"username":"杨凯","user_valid":True,"root_id":"2","doc_id":"27","params":{"ts_code":ts_code,"trade_date":"","start_date": start_date,"end_date": end_date,"offset":"","limit":""},"fields":["ts_code","trade_date","open","high","low","close","pre_close","change","pct_chg","vol","amount"]}
    url = 'https://tushare.pro/wctapi/apis/daily'
    result = request(url, json.dumps(data))
    StockDateLine = json.loads(result)
    tsCodeList = [item['ts_code'] for item in dateLineMongo.find()]
    item = {}
    item['ts_code'] = ts_code
    StockDateLineList = StockDateLine['data']['items']
    item['data_line'] = [{
        'ts_code': stock[0],
        'trade_date': stock[1],
        'open': stock[2],
        'high': stock[3],
        'low': stock[4],
        'close': stock[5],
        'pre_close': stock[6],
        'change': stock[7],
        'vol': stock[8],
        'amount': stock[9]
    } for stock in StockDateLineList]
    if item['ts_code'] in tsCodeList:
        dateLineMongo.update_one({'ts_code': item['ts_code']}, {'$set': {'dateline': item['data_line']}})
    else:
        dateLineMongo.insert(item)

def getStockDateLineAll():
    start_date = time.strftime('%Y%m%d', time.localtime(int(time.time() - 24*60*60*30)))
    end_date = time.strftime('%Y%m%d', time.localtime(int(time.time())))
    ts_codes = [item['ts_code'] for item in codeMongo.find()]
    for ts_code in ts_codes:
        getStockDateLine(ts_code, start_date, end_date)


if __name__ == '__main__':
    getStockNameInfo()