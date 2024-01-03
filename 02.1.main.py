# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

gameMatrix = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

def checkOneLine(line):
    moveO = ord(line[0]) - 65
    moveY = ord(line[2]) - 88
    return gameMatrix[moveO][moveY] + moveY + 1

with open('02.input.txt', 'r') as file:
    counter = 0;
    for line in file:
        counter += checkOneLine(line)
    print(counter)
