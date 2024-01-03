# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

def find(matrix, letter):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if (matrix[i][j] == ord(letter)):
                return i, j

matrix = []
with open('12.input.txt', 'r') as file:
    for line in file:
        row = [ord(letter) for letter in line[ : -1]]
        matrix.append(row)

start = find(matrix, 'S')
end = find(matrix, 'E')
matrix[start[0]][start[1]] = ord('a')
matrix[end[0]][end[1]] = ord('z')

n = len(matrix)
m = len(matrix[0])
visited = [[0 for j in range(m)] for i in range(n)]

found = False
step = 1
visited[start[0]][start[1]] = step

while not found:
    for i in range(0, n):
        for j in range(0, m):
            if (visited[i][j] == step):
                if (i > 0 and visited[i - 1][j] == 0 and matrix[i - 1][j] - matrix[i][j] < 2):
                    visited[i - 1][j] = step + 1
                if (i < n - 1 and visited[i + 1][j] == 0 and matrix[i + 1][j] - matrix[i][j] < 2):
                    visited[i + 1][j] = step + 1
                if (j > 0 and visited[i][j - 1] == 0 and matrix[i][j - 1] - matrix[i][j] < 2):
                    visited[i][j - 1] = step + 1
                if (j < m - 1 and visited[i][j + 1] == 0 and matrix[i][j + 1] - matrix[i][j] < 2):
                    visited[i][j + 1] = step + 1
    step += 1
    if (visited[end[0]][end[1]] > 0):
        found = True    

print(step - 1)
