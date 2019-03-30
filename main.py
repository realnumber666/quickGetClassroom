#coding:utf-8
import requests
import re
import json
from bs4 import BeautifulSoup

url = "http://hub.m.hust.edu.cn/aam/room/selectFreeRoom.action?buildingCode=%27D120,%E4%B8%9C%E5%8D%81%E4%BA%8C%E6%A5%BC%27&borrowDate=%272019-03-30%27&section=%279-10%E8%8A%82%27"

headers = {'Cookie': 'JSESSIONID=0000J2XFamfH9Aqe6oR0g0xW4lZ:-1'}
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.content)
i = 0
pattern = re.compile("var json='(.*?)';")
# for child in soup.html.contents:
#     i+=1
#     print('--------'+str(i))
#     print(child)
jsScript = soup.html.contents[5].string
jsScript = jsScript.strip().replace('\n','')
m = pattern.match(jsScript).groups()[0]
j = json.loads(m)
list = j['dataList']
rooms = []
for item in list:
    room = item['JSMC']
    rooms.append(room)
print(rooms)
