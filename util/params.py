#coding=utf-8
__author__ = 'kai.yang'
__date__ = '2022/7/5 21:55'

ROSE_NUMBER = 2
GET_OPTIONAL_URL = 'https://d.10jqka.com.cn/multimarketreal/hs/{code}/1968584_13_19_3541450_526792_6_7_8_9_10_2034120_199112_264648?callback=multimarketreal'
GET_KLINE_URL = 'https://d.10jqka.com.cn/v2/time/{code}/last.js'

TONGHUASHUN_HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'https://t.10jqka.com.cn/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

WENCAI_HEADERS = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'Cache-control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'v=A60f97F7s8Qnllcoo6XDIayfvEIiCuEFaz9Fqu-y6W6xlcO8t1rxrPuOVY18',
  'Origin': 'http://www.iwencai.com',
  'Pragma': 'no-cache',
  'Referer': 'http://www.iwencai.com/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
  'envtag': 'yzg'
}