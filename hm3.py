# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:23:38 2021

@author: USER
"""
#新北市公共自行車租賃系統

import requests
import json

url ='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json/preview'
data=requests.get(url).text
tax=json.loads(data)

for item in tax:
    print('站點代號:',item['sno'])
    print('站點:',item['sna'])
    print('總停車格:',item['tot'])  
    print('可借車輛:',item['sbi'])  
    print('可還空位:',item['bemp'])  
    print('地址:',item['ar'])      
    print()