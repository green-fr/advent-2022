# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

cubes = []

fileName = '18.input.txt'
with open(fileName, 'r') as file:
    for line in file:
        parsedLine = line.split(',')
        cube = [int(x) for x in parsedLine]
        cubes.append(cube)

def distance(cube1, cube2):
    return abs(cube1[0] - cube2[0]) + abs(cube1[1] - cube2[1]) + abs(cube1[2] - cube2[2])
touches = 0
for i in range(len(cubes)):
    for j in range(i + 1, len(cubes)):
        if (distance(cubes[i], cubes[j]) == 1):
            touches += 1

print(len(cubes) * 6 - 2 * touches)
