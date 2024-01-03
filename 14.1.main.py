# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""
fileName = '14.input.txt'
xMin = 500
xMax = 500
yMax = 0
with open(fileName, 'r') as file:
    for line in file:
        parsedLine = line[ : -1].split(' -> ')
        for i in range(len(parsedLine)):
            x, y = parsedLine[i].split(',')
            x = int(x)
            y = int(y)
            if (x < xMin): xMin = x
            if (x > xMax): xMax = x
            if (y > yMax): yMax = y

maze = [[0 for j in range(xMax - xMin + 1)] for i in range(yMax + 1)]

def drawLine(pointFrom, pointTo):
    print(pointFrom, pointTo)
    if (pointFrom[0] == pointTo[0]):
        # Vertical line
        i = pointFrom[0]
        for j in range(min(pointFrom[1], pointTo[1]), max(pointFrom[1], pointTo[1]) + 1):
            maze[j][i - xMin] = 1
    else:
        # Horizontal line
        j = pointFrom[1]
        for i in range(min(pointFrom[0], pointTo[0]), max(pointFrom[0], pointTo[0]) + 1):
            maze[j][i - xMin] = 1

with open(fileName, 'r') as file:
    for line in file:
        parsedLine = line[ : -1].split(' -> ')
        pointFrom = None
        for i in range(len(parsedLine)):
            x, y = parsedLine[i].split(',')
            x = int(x)
            y = int(y)
            pointTo = (x, y)
            if (pointFrom != None):
                drawLine(pointFrom, pointTo)
            pointFrom = pointTo

for line in maze: print(line)

nbSand = 0
globalGoing = True
while (globalGoing):
    nbSand += 1
    sand = (0, 500 - xMin)
    localGoing = True
    while (localGoing):
        if (sand[0] == yMax):
            localGoing = False
            globalGoing = False
        elif (maze[sand[0] + 1][sand[1]] == 0):
            sand = (sand[0] + 1, sand[1])
        elif (sand[1] == 0):
            localGoing = False
            globalGoing = False
        elif (maze[sand[0] + 1][sand[1] - 1] == 0):
            sand = (sand[0] + 1, sand[1] - 1)
        elif (sand[1] == xMax - xMin):
            localGoing = False
            globalGoing = False
        elif (maze[sand[0] + 1][sand[1] + 1] == 0):
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            maze[sand[0]][sand[1]] = 2
            localGoing = False
            
for line in maze: print(line)
print(nbSand - 1)
