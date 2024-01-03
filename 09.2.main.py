# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

import numpy as np

rope = np.zeros((10, 2), int)
visited = set()

def moveNext(h, t):
    d = h - t
    if (abs(d[0]) > 1) or (abs(d[1]) > 1):
        t[0] += np.sign(d[0])
        t[1] += np.sign(d[1])
    return t
    
with open('09.input.txt', 'r') as file:
    for line in file:
        #print(line)
        direction, length = line.split(' ')
        length = int(length)
        for i in range(0, length):
            if (direction == 'U'):
                rope[0][0] -= 1
            elif (direction == 'D'):
                rope[0][0] += 1
            elif (direction == 'R'):
                rope[0][1] += 1
            elif (direction == 'L'):
                rope[0][1] -= 1
            for j in range(1, 10):
                rope[j] = moveNext(rope[j - 1], rope[j])
            visited.add(tuple(rope[9]))
            #print(visited)
print(len(visited))
