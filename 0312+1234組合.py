# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:10:17 2021

@author: yu
"""
count=0

for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x!=y) and (y!=z) and (z!=x):
                print("%d%d%d" % (x, y, z))
                count+=1
print('總共有',count,"種組合")