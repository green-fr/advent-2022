# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

fileName = '17.input small.txt'
with open(fileName, 'r') as file:
    for line in file:
        wind = line.rstrip()

tetris = []
tetris.append([[1, 1, 1, 1]])
tetris.append([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
tetris.append([[1, 1, 1], [0, 0, 1], [0, 0, 1]])
tetris.append([[1], [1], [1], [1]])
tetris.append([[1, 1], [1, 1]])
n = 7
m = 4000
chamber = [[0 for j in range(n)] for i in range(m)]
for i in range(n):
    chamber[0][i] = 1
top = 0
wIndex = 0

def getNewPosition(position, direction):
    # print(position, direction)
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
            if (piece[j][i] == 1 and chamber[position[0] + j][position[1] + i] == 1):
                return False
    return True

def addPiece(chamber, piece, position, top):
    for j in range(len(piece)):
        for i in range(len(piece[j])):
            if (piece[j][i] == 1):
                chamber[position[0] + j][position[1] + i] = 1
                top = max(top, position[0] + j)
    return top
    
pieces = 2022
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
    # print()
    # for line in chamber:
    #     print(line)
    # print()
print(top)
