# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 13:43:49 2023

@author: green
"""

with open('01.input.txt', 'r') as file:
    counter = 0;
    currentMax = 0;
    for line in file:
        if (line == '\n'):
            if (counter > currentMax):
                currentMax = counter
            counter = 0
        else:
            counter += int(line)
    print(currentMax)
