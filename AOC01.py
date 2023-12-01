# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:07:56 2022

@author: Benjamin
"""
import re

numbers = {"one":1, "two":2, "three":3, "four": 4, "five": 5, "six":6, "seven":7, "eight":8, "nine":9}

with open('input.txt') as file:
    inp = file.read().split("\n")

accumulator = 0
accumulator1 = 0
for line in inp:
    nums1 = re.findall(r'\d',line)
    nums = re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine|ten))', line)
    if(len(nums1)>0):
        accumulator1 += 10*int(nums1[0])+int(nums1[-1])
    nums = [num.group(1) for num in nums]
    if(len(nums)>0):
        if(len(nums[0])==1):
            a = int(nums[0])
        else:
            a = numbers[nums[0]]
        if(len(nums[-1])==1):
            b = int(nums[-1])
        else:
            b = numbers[nums[-1]]
        accumulator += 10*a+b
print(accumulator1) 
print(accumulator)