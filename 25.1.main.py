# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green

"""
import re

charValue = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
snafuValues = {value: key for key, value in charValue.items()}
def dec2snafu(dec):
    five = [0] + dec2five(dec)
    for i in range(len(five) - 1, 0, -1):
        if (five[i] > 2):
            five[i - 1] += 1
            five[i] -= 5
    snafu = ''
    for i in range(len(five)):
        snafu += snafuValues.get(five[i])
    snafu = re.sub(r'^0+', '', snafu)
    return snafu
def dec2five(dec):
    five = []
    base = 5
    while (dec > 0):
        five = [dec % base] + five
        dec //= base
    return five
def snafu2dec(dec):
    snafu = 0
    for i in range(len(dec)):
        snafu = snafu * 5 + charValue.get(dec[i])
    return snafu

counter = 0
with open('25.input.txt', 'r') as file:
    for line in file:
        counter += snafu2dec(line.rstrip())
print(counter)
# print(dec2five(counter))
print(dec2snafu(counter))
