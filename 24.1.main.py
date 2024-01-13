# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green

"""

with open('24.input.txt', 'r') as file:
    lines = file.readlines()
n = len(lines) - 2
m = len(lines[0]) - 3
blizzards = []
directions = []
for i in range(n):
    for j in range(m):
        char = lines[i + 1][j + 1]
        if (char != '.'):
            blizzards.append((i, j))
            directions.append(char)

def moveBlizzards():
    for i in range(len(blizzards)):
        if (directions[i] == 'v'):
            blizzards[i] = ((blizzards[i][0] + 1) % n, blizzards[i][1])
        elif (directions[i] == '^'):
            blizzards[i] = ((blizzards[i][0] - 1) % n, blizzards[i][1])
        elif (directions[i] == '>'):
            blizzards[i] = (blizzards[i][0], (blizzards[i][1] + 1) % m)
        elif (directions[i] == '<'):
            blizzards[i] = (blizzards[i][0], (blizzards[i][1] - 1) % m)

def checkCase(position):
    if (0 <= position[0] < n and 0 <= position[1] < m):
        if (not position in blizzards):
            accessible.add(position)
    
accessible = set()
day = 0
# print(day, blizzards)
# print(day, accessible)
while True:
    day += 1
    moveBlizzards()
    previous = accessible.copy()
    accessible = set()
    if (not (0, 0) in blizzards):
        accessible.add((0, 0))
    for loop in previous:
        checkCase(loop)
        checkCase((loop[0] - 1, loop[1]))
        checkCase((loop[0] + 1, loop[1]))
        checkCase((loop[0], loop[1] - 1))
        checkCase((loop[0], loop[1] + 1))
    if ((n - 1, m - 1) in accessible):
        print(day + 1)
        break
    # print(day, blizzards)
    # print(day, accessible)
    