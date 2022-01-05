#!/usr/bin/python     assignment-2.py
# -*- coding: utf-8 -*-

# 1
def calculate(min, max):
    sun = 0
    for num in range(min,max+1):
        sun += num
    print(sun)

calculate(1, 3) 
calculate(4, 8) 


#2 
def avg(data):
    salaryTotal = 0
    for employees in data['employees']:
       salaryTotal+=employees['salary']
    print(salaryTotal/data['count'])
avg({
"count":3,
"employees":[
    {
        "name":"John",
        "salary":30000
    },

    {
        "name":"Bob",
        "salary":60000
    },
    {
        "name":"Jenny",
        "salary":50000
    }
]
}) # 呼叫 avg 函式


#3
def maxProduct(nums):
    bubbleSort(nums)
    MaxNum1 = nums[-1]
    MaxNum2 = nums[-2]
    print( MaxNum1 * MaxNum2) 
    
def bubbleSort(arry):
    n = len(arry)
    for i in range(n - 2):
        for j in range(n-i-1):
            if arry[j] > arry[j+1]:
                arry[j], arry[j+1] = arry[j+1], arry[j]

# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0


#4
def twoSum(nums, target):
    x = len(nums)
    for i in range(0 ,x):
        for j in range(0 ,x):
            if nums[i] + nums[j] == target:
                return nums[i] , nums[j]
        
# your code here
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9