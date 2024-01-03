# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

import numpy as np

h = np.array([0, 0])
t = np.array([0, 0])
visited = set()

with open('09.input.txt', 'r') as file:
    for line in file:
        #print(line)
        direction, length = line.split(' ')
        length = int(length)
        for i in range(0, length):
            if (direction == 'U'):
                h[0] -= 1
            elif (direction == 'D'):
                h[0] += 1
            elif (direction == 'R'):
                h[1] += 1
            elif (direction == 'L'):
                h[1] -= 1
            d = h - t
            if (abs(d[0]) > 1) or (abs(d[1]) > 1):
                t[0] += np.sign(d[0])
                t[1] += np.sign(d[1])
            visited.add(tuple(t))
            #print(visited)
print(len(visited))
