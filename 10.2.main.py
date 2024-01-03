# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""


x = 1
ticker = 0
image = ''

def getPixel(x, ticker):
    column = ticker % 40
    if (abs(column - x) < 2):
        return '#'
    else:
        return '.'
    
with open('10.input.txt', 'r') as file:
    for line in file:
        parsedLine = line.split(' ')
        if (parsedLine[0] == 'noop\n'):
            image += getPixel(x, ticker)
            ticker += 1
        elif (parsedLine[0] == 'addx'):
            image += getPixel(x, ticker)
            ticker += 1
            image += getPixel(x, ticker)
            ticker += 1
            x += int(parsedLine[1])
print(image[0 : 40])
print(image[40 : 80])
print(image[80 : 120])
print(image[120 : 160])
print(image[160 : 200])
print(image[200 : 240])

