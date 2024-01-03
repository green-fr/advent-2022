# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

def allDifferent(stack):
    return len(set(stack)) == len(stack)

windowSize = 14
with open('06.input.txt', 'r') as file:
    for line in file:
        for i in range(windowSize, len(line)):
            if (allDifferent(line[i - windowSize : i])):
                print(i)
                break
