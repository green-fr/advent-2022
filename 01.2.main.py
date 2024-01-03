# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 13:43:49 2023

@author: green
"""

def checkTop(currentTop, counter):
    currentTop.append(counter)
    currentTop.sort()
    return currentTop[-3:]

with open('01.input.txt', 'r') as file:
    counter = 0;
    currentTop = [0, 0, 0];
    for line in file:
        if (line == '\n'):
            currentTop = checkTop(currentTop, counter)
            counter = 0
        else:
            counter += int(line)
    print(currentTop)
    print(sum(currentTop))
    