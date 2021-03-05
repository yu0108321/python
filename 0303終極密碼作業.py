# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:04:29 2021

@author: USER
"""
import random

min=1
max=100

count=0
ans=random.randint(min,max)
guess=0

while ans !=guess:
    guess=int(input("請輸入1~100之間的整數:"))
    count+=1 
    if guess <= min or guess>=max:
        print("請輸入",min,"~",max,"之間")   
        
    elif guess < ans:
        min=guess
        print(min,"~",max,"，之間請繼續")
         
    elif guess > ans:
        max=guess
        print(min,"~",max,"，之間請繼續")
           
print("猜對了,共猜了",count,"次")