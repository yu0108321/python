# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:23:38 2021

@author: USER
"""
#新北市公有路外停車場即時賸餘車位數

import requests
import json

url ='https://data.ntpc.gov.tw/api/datasets/E09B35A5-A738-48CC-B0F5-570B67AD9C78/json/preview'
data=requests.get(url).text
tax=json.loads(data)

for item in tax:
    print('停車場編號:',item['id'])
    print('停車場剩餘車位數:',item['availableCar'])  
    print()