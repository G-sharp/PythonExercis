#-*- coding=utf-8 -*-
import requests
from lxml import html
url='https://movie.douban.com/typerank?type_name=喜剧&type=24&interval_id=100:90&action=' #需要爬数据的网址
page=requests.Session().get(url)
tree=html.fromstring(page.text)
result=tree.xpath('//div[@class="types"]//span//a/text()') #获取需要的数据
for ch in result:
    print (ch)
