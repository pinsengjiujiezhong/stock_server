#coding=utf-8

def parse_pandas(data):
    column_list = []
    for row in data:
        column_list.append(row)
    jsonlist = []
    for index in range(data[column_list[0]].size):
        dict = {}
        for row in data:
            dict[row] = data[row][index]
        jsonlist.append(dict)
    return jsonlist
