# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

changeMatrix = [
    [2, 0, 1],
    [0, 1, 2],
    [1, 2, 0]
]
gameMatrix = [
    [3, 6, 0],
    [0, 3, 6],
    [6, 0, 3]
]

def checkOneLine(line):
    moveO = ord(line[0]) - 65
    preMoveY = ord(line[2]) - 88
    moveY = changeMatrix[moveO][preMoveY]
    return gameMatrix[moveO][moveY] + moveY + 1

with open('02.input.txt', 'r') as file:
    counter = 0;
    for line in file:
        counter += checkOneLine(line)
        print(counter)
