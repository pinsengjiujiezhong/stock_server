#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2022/7/28 20:37'

#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2022/7/27 21:30'
import platform


if platform.system().lower() == 'windows':
    from util.db import fundMongo, fundPositionMongo
elif platform.system().lower() == 'linux':
    from db import fundMongo, fundPositionMongo


def fundPosition():
    funds = fundMongo.find({})
    positions = []
    for fund in funds:
        names = [item['name'] for item in positions]
        for position in fund['positions']:
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
    for item in positions:
        item['proportion'] = int(item['proportion'])
        fundPositionMongo.insert_one(item)


if __name__ == '__main__':
    fundPosition()
