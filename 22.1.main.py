# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

with open('22.input.txt', 'r') as file:
    counter = 0;
    lines = file.readlines()
maze = [lines[i].rstrip() for i in range(len(lines) - 2)]
n = len(maze)
m = 0
for i in range(n):
    m = max(m, len(maze[i]))
for i in range(n):
    maze[i] += ' ' * (m - len(maze[i]))

path = lines[-1]
for line in maze:
    print(line)
print(path)

pathParsed = []
currentGroup = ''
currentChars = False
for char in path:
    if char.isalpha():
        if (not currentChars):
            currentChars = True
            pathParsed.append(int(currentGroup))
            currentGroup = ''
        currentGroup += char
    elif char.isdigit():
        if (currentChars):
            currentChars = False
            pathParsed.append(currentGroup)
            currentGroup = ''
        currentGroup += char
if (currentChars):
    pathParsed.append(currentGroup)
else:
    pathParsed.append(int(currentGroup))
print(pathParsed)

def findStartingPosition():
    for i, char in enumerate(maze[0]):
        if char not in [' ', '#']:
            return (0, i, 0)

position = findStartingPosition()
print(position)
for instruction in pathParsed:
    if (instruction == 'R'):
        position = (position[0 : 2]) + ((position[2] + 1) % 4,)
    elif (instruction == 'L'):
        position = (position[0 : 2]) + ((position[2] - 1) % 4,)
    else:
        for i in range(instruction):
            newPosition = position
            repeat = True
            while (repeat):
                if (position[2] == 0):
                    newPosition = (newPosition[0], (newPosition[1] + 1) % m, newPosition[2])
                elif (position[2] == 1):
                    newPosition = ((newPosition[0] + 1) % n, newPosition[1], newPosition[2])
                elif (position[2] == 2):
                    newPosition = (newPosition[0] , (newPosition[1] - 1) % m, newPosition[2])
                elif (position[2] == 3):
                    newPosition = ((newPosition[0] - 1) %n, newPosition[1], newPosition[2])
                repeat = (maze[newPosition[0]][newPosition[1]] == ' ')
            if (maze[newPosition[0]][newPosition[1]] == '#'):
                break
            else:
                position = newPosition
    print(instruction, position)

print((position[0] + 1) * 1000 + (position[1] + 1) * 4 + position[2])
