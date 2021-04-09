# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:23:38 2021

@author: USER
"""
#台南自行車

import requests
import json

url ='http://tbike-data.tainan.gov.tw/Service/StationStatus/Json'
data=requests.get(url).text
tax=json.loads(data)

for item in tax:
    print('站名:',item['StationName'])
    print('總空間:',item['Capacity'])  
    print('可借:',item['AvaliableBikeCount'])
    print('可停:',item['AvaliableSpaceCount'])    
    print()