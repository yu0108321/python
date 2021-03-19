# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:58:14 2021

@author: yu
"""

for i in range(1, 10):
    for j in range(1, 10):
        print(str(i) + 'x' + str(j) + '=' + str(i * j) + ' ', end='')
    print()