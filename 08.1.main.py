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
counter = 0
n = len(matrix)
for i in range(1, n - 1):
    for j in range(1, n - 1):
        visible = False
        if (all(matrix[i][j1] < matrix[i][j] for j1 in range(0, j))):
            visible = True
        if (all(matrix[i][j1] < matrix[i][j] for j1 in range(j + 1, n))):
            visible = True
        if (all(matrix[i1][j] < matrix[i][j] for i1 in range(0, i))):
            visible = True
        if (all(matrix[i1][j] < matrix[i][j] for i1 in range(i + 1, n))):
            visible = True
        if (visible):
            #print(i, j)
            counter += 1
        visibleTop = True
        for i1 in range(0, i):
            if (matrix[i1][j] >= matrix[i][j]):  visibleTop = False
        visibleBottom = True
        for i1 in range(i + 1, n):
            if (matrix[i1][j] >= matrix[i][j]):  visibleBottom = False
        visibleLeft = True
        for j1 in range(0, j):
            if (matrix[i][j1] >= matrix[i][j]):  visibleLeft = False
        visibleRight = True
        for j1 in range(j + 1, n):
            if (matrix[i][j1] >= matrix[i][j]):  visibleRight = False
        newVisible = visibleTop or visibleBottom or visibleLeft or visibleRight
        if (not visible == newVisible):
            print(i, j)
        
print(counter + 4 * (n - 1))
