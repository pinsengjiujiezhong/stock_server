import pymysql
import json, time
import platform

if platform.system().lower() == 'windows':
    from util.db import codeMongo, dateLineMongo, roseMongo
    from util.params import PRO
    from util.get_tushare import parse_pandas
elif platform.system().lower() == 'linux':
    from db import codeMongo, dateLineMongo, roseMongo


def getRose():
    dateLines = dateLineMongo.find()
    ts_codes = [item['ts_code'] for item in roseMongo.find()]
    for dateLine in dateLines:
        if dateLine['ts_code'][:2] in ['30', '68']:
            continue
        trendList = []
        dates = []
        prices = []
        previous = num = 0
        monthprevious = monthnum = 0
        for daily in dateLine['date_line']:
            trendList.append({'date': daily['trade_date'], 'price': daily['close']})
            dates.append(daily['trade_date'])
            prices.append(daily['close'])
        for daily in dateLine['date_line']:
            if not previous:
                previous = daily['close']
                continue
            if previous > daily['close']:
                num += 1
                previous = daily['close']
            else:
                break
        for daily in dateLine['date_line']:
            if not monthprevious:
                monthprevious = daily['close']
                continue
            if monthprevious > daily['close']:
                monthnum += 1
            monthprevious = daily['close']
        item = {
            'code': dateLine['ts_code'][:6],
            'ts_code': dateLine['ts_code'],
            'name': codeMongo.find_one({'ts_code': dateLine['ts_code']})['name'],
            'trend': trendList,
            'num': num,
            'monthnum': monthnum,
            'dates': dates,
            'prices': prices,
        }
        print('item: ', item['ts_code'])
        if dateLine['ts_code'] in ts_codes:
            roseMongo.delete_one({'ts_code': dateLine['ts_code']})
        roseMongo.insert_one(item)


def prints():
    print(int(time.time()))


if __name__ == '__main__':
    getRose()



