import pymysql
import json, time
from util.params import ROSE_NUMBER
from util.db import codeMongo, dateLineMongo, roseMongo



def getRose():
    dateLines = dateLineMongo.find()
    for dateLine in dateLines:
        trendList = []
        dates = []
        prices = []
        ts_codes = [item['ts_code'] for item in roseMongo.find()]
        for daily in dateLine['data_line']:
            trendList.append({'date': daily['trade_date'], 'price': daily['pre_close']})
            dates.append(daily['trade_date'])
            prices.append(daily['pre_close'])
        previous = num = 0
        if dateLine['ts_code'] in ['30', '68']:
            continue
        for daily in dateLine['data_line']:
            if not previous:
                previous = daily['pre_close']
                continue
            if previous > daily['pre_close']:
                num += 1
                previous = daily['pre_close']
            else:
                break
        print(daily, num)
        item = {
            'code': dateLine['ts_code'][:6],
            'ts_code': dateLine['ts_code'],
            'name': codeMongo.find_one({'ts_code': dateLine['ts_code']})['name'],
            'trend': trendList,
            'num': num,
            'dates': dates,
            'prices': prices,
        }
        print('item: ', item)
        if dateLine['ts_code'] in ts_codes:
            roseMongo.delete_one({'ts_code': dateLine['ts_code']})
        roseMongo.insert(item)


def prints():
    print(int(time.time()))


if __name__ == '__main__':
    getRose()



