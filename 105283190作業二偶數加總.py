# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
sum=0

number=int(input("請輸入次數:"))
for i in range(1,number+1):
     if i%2 ==0:
      sum+=i
      print(i)
print("上面數字皆是偶數")
print("上面加總為",sum)
print("程式執行完畢")