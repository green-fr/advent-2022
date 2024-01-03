# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

matrix = []
with open('08.input.txt', 'r') as file:
    for line in file:
        row = [int(digit) for digit in line[ : -1]]
        matrix.append(row)
maxCounter = 0
n = len(matrix)
for i in range(1, n - 1):
    for j in range(1, n - 1):
        counter = 1
        subCounter = 0
        for i1 in range(i - 1, -1, -1):
            subCounter += 1
            if (matrix[i1][j] >= matrix[i][j]):  break
        counter *= subCounter
        subCounter = 0
        for i1 in range(i + 1, n):
            subCounter += 1
            if (matrix[i1][j] >= matrix[i][j]):  break
        counter *= subCounter
        subCounter = 0
        for j1 in range(j - 1, -1, -1):
            subCounter += 1
            if (matrix[i][j1] >= matrix[i][j]):  break
        counter *= subCounter
        subCounter = 0
        for j1 in range(j + 1, n):
            subCounter += 1
            if (matrix[i][j1] >= matrix[i][j]):  break
        counter *= subCounter
        #print(i, j, counter)
        if (counter > maxCounter): maxCounter = counter
print(maxCounter)
