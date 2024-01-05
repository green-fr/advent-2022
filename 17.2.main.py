# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

fileName = '17.input.txt'
with open(fileName, 'r') as file:
    for line in file:
        wind = line.rstrip()

tetris = []
tetris.append([[True, True, True, True]])
tetris.append([[False, True, False], [True, True, True], [False, True, False]])
tetris.append([[True, True, True], [False, False, True], [False, False, True]])
tetris.append([[True], [True], [True], [True]])
tetris.append([[True, True], [True, True]])
n = 7
m = 100
chamber = [[False for j in range(n)] for i in range(m)]
for i in range(n):
    chamber[0][i] = True
bottom = [0 for j in range(n)]

def getNewPosition(position, direction):
    if (direction == '<'):
        position = (position[0], position[1] - 1)
    elif (direction == '>'):
        position = (position[0], position[1] + 1)
    elif (direction == '|'):
        position = (position[0] - 1, position[1])
    return position
    
def isPossible(chamber, piece, position):
    if (position[1] < 0):
        return False
    if (position[1] + len(piece[0]) > n):
        return False
    for j in range(len(piece)):
        for i in range(len(piece[j])):
            if (piece[j][i] and chamber[position[0] + j][position[1] + i]):
                return False
    return True

def addPiece(chamber, piece, position, top):
    for j in range(len(piece)):
        for i in range(len(piece[j])):
            if (piece[j][i]):
                chamber[position[0] + j][position[1] + i] = True
                top = max(top, position[0] + j)
                bottom[position[1] + i] = max(bottom[position[1] + i], position[0] + j)
    return top
    
top = 0
wIndex = 0
cutted = 0
pieces = 3290
cutHistory = []
for p in range(pieces):
    piece = tetris[p % len(tetris)]
    position = (top + 4, 2)
    falling = True
    while (falling):
        newPosition = getNewPosition(position, wind[wIndex % len(wind)])
        if (isPossible(chamber, piece, newPosition)):
            position = newPosition
        wIndex += 1
        newPosition = getNewPosition(position, '|')
        if (isPossible(chamber, piece, newPosition)):
            position = newPosition
        else:
            falling = False
    top = addPiece(chamber, piece, position, top)
    cutLevel = min(bottom)
    if (cutLevel > 0):
        # Find a cycle of cuts, analyse one cut result and remaining of a huge number
        cutHistory.append([cutLevel, p])
        chamber = chamber[cutLevel : ] + [[False for j in range(n)] for i in range(cutLevel)]
        cutted += cutLevel
        for i in range(n):
            bottom[i] -= cutLevel
        top -= cutLevel
print(top + cutted)

