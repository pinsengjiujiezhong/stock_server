from django.test import TestCase

# Create your tests here.
import requests

url = "http://ai.iwencai.com/urp/v7/landing/getDataList"

payload=payload='query=%E6%98%A8%E6%97%A5%E6%B6%A8%E5%81%9C&urp_sort_way=desc&page=1&perpage=50&condition=%5B%7B%22dateText%22%3A%22%E6%98%A8%E6%97%A5%22%2C%22indexName%22%3A%22%E6%B6%A8%E5%81%9C%22%2C%22indexProperties%22%3A%5B%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%2020220708%22%5D%2C%22dateUnit%22%3A%22%E6%97%A5%22%2C%22source%22%3A%22new_parser%22%2C%22type%22%3A%22index%22%2C%22indexPropertiesMap%22%3A%7B%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%3A%2220220708%22%7D%2C%22reportType%22%3A%22TRADE_DAILY%22%2C%22dateType%22%3A%22%E4%BA%A4%E6%98%93%E6%97%A5%E6%9C%9F%22%2C%22chunkedResult%22%3A%22%E6%98%A8%E6%97%A5%E6%B6%A8%E5%81%9C%22%2C%22valueType%22%3A%22_%E6%98%AF%E5%90%A6%22%2C%22domain%22%3A%22abs_%E8%82%A1%E7%A5%A8%E9%A2%86%E5%9F%9F%22%2C%22uiText%22%3A%22%E6%98%A8%E6%97%A5%E7%9A%84%E6%B6%A8%E5%81%9C%22%2C%22sonSize%22%3A0%2C%22queryText%22%3A%22%E6%98%A8%E6%97%A5%E7%9A%84%E6%B6%A8%E5%81%9C%22%2C%22relatedSize%22%3A0%2C%22tag%22%3A%22%5B%E6%98%A8%E6%97%A5%5D%E6%B6%A8%E5%81%9C%22%7D%5D&comp_id=6257151&business_cat=soniu&uuid=24087'
headers = {
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

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
