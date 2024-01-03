# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""


x = 1
ticker = 0
counter = 0

with open('10.input.txt', 'r') as file:
    for line in file:
        parsedLine = line.split(' ')
        #print(line, ticker, x)
        if (parsedLine[0] == 'noop\n'):
            ticker += 1
        elif (parsedLine[0] == 'addx'):
            ticker += 1
        if ((ticker - 20) % 40 == 0):
            counter += x * ticker
            #print(ticker, x)
        if (parsedLine[0] == 'addx'):
            ticker += 1
            if ((ticker - 20) % 40 == 0):
                counter += x * ticker
                #print(ticker, x)
        if (parsedLine[0] == 'addx'):
            x += int(parsedLine[1])
print(counter)
