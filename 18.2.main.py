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
        cube = [int(x) + 1 for x in parsedLine]
        cubes.append(cube)

def distance(cube1, cube2):
    return abs(cube1[0] - cube2[0]) + abs(cube1[1] - cube2[1]) + abs(cube1[2] - cube2[2])

touches = 0
for i in range(len(cubes)):
    for j in range(i + 1, len(cubes)):
        if (distance(cubes[i], cubes[j]) == 1):
            touches += 1

print(len(cubes) * 6 - 2 * touches)

maxX = 0
maxY = 0
maxZ = 0
for i in range(len(cubes)):
    maxX = max(maxX, cubes[i][0])
    maxY = max(maxY, cubes[i][1])
    maxZ = max(maxZ, cubes[i][2])

visited = [[[0 for i in range(maxZ + 2)] for j in range(maxY + 2)] for k in range(maxX + 2)]

for i in range(len(cubes)):
    cube = cubes[i]
    visited[cube[0]][cube[1]][cube[2]] = -1

for x in range(maxX + 2):
    for y in range(maxY + 2):
        for z in range(maxZ + 2):
            visited[0][y][z] = 1
            visited[x][0][z] = 1
            visited[x][y][0] = 1
            visited[maxX + 1][y][z] = 1
            visited[x][maxY + 1][z] = 1
            visited[x][y][maxZ + 1] = 1

def setIfAvailable(x, y, z, wave):
    if (x in range(len(visited)) and y in range(len(visited[0])) and z in range(len(visited[0][0]))):
        if (visited[x][y][z] == 0):
            visited[x][y][z] = wave + 1
    
wave = 0
dirty = True
while (dirty):
    wave += 1
    dirty = False
    for x in range(maxX + 2):
        for y in range(maxY + 2):
            for z in range(maxZ + 2):
                if (visited[x][y][z] == wave):
                    dirty = True
                    setIfAvailable(x - 1, y, z, wave)
                    setIfAvailable(x + 1, y, z, wave)
                    setIfAvailable(x, y - 1, z, wave)
                    setIfAvailable(x, y + 1, z, wave)
                    setIfAvailable(x, y, z - 1, wave)
                    setIfAvailable(x, y, z + 1, wave)

vides = []
for x in range(maxX + 2):
    for y in range(maxY + 2):
        for z in range(maxZ + 2):
            if (visited[x][y][z] == 0):
                vides.append([x, y, z])

touchesVide = 0
for i in range(len(vides)):
    for j in range(i + 1, len(vides)):
        if (distance(vides[i], vides[j]) == 1):
            touchesVide += 1

print(len(vides) * 6 - 2 * touchesVide)

print(len(cubes) * 6 - 2 * touches - (len(vides) * 6 - 2 * touchesVide))
