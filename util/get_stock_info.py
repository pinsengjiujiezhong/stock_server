#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2022/7/8 21:56'
import platform


if platform.system().lower() == 'windows':
    from util.db import codeMongo, dateLineMongo
    from util.params import PRO
    from util.get_tushare import parse_pandas
elif platform.system().lower() == 'linux':
    from db import codeMongo, dateLineMongo
    from params import PRO
    from get_tushare import parse_pandas
import time


def getStockNameInfo():
    data = PRO.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    stockInfoList = parse_pandas(data)
    symbolList = [item['symbol'] for item in codeMongo.find()]
    for stock in stockInfoList:
        if stock['symbol'] in symbolList:
            continue
        codeMongo.insert_one(stock)


def getStockDateLine(ts_code, start_date, end_date, tsCodeList):
    data = PRO.query('daily', ts_code=ts_code, start_date=start_date, end_date=end_date)
    item = {}
    item['ts_code'] = ts_code
    item['date_line'] = parse_pandas(data)
    print(item['ts_code'])
    if item['ts_code'] in tsCodeList:
        dateLineMongo.update_one({'ts_code': item['ts_code']}, {'$set': {'date_line': item['date_line']}})
    else:
        dateLineMongo.insert_one(item)


def getStockDateLineAll():
    start_date = time.strftime('%Y%m%d', time.localtime(int(time.time() - 24*60*60*30)))
    end_date = time.strftime('%Y%m%d', time.localtime(int(time.time())))
    ts_codes = [item['ts_code'] for item in codeMongo.find()]
    tsCodeList = [item['ts_code'] for item in dateLineMongo.find()]
    for ts_code in ts_codes:
        time.sleep(0.1)
        getStockDateLine(ts_code, start_date, end_date, tsCodeList)


if __name__ == '__main__':
    print(1)
    # getStockNameInfo()
    getStockDateLineAll()
