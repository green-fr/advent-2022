# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

numbers = []
positions = []
indexZero = []
i = 0
fileName = '20.input.txt'
with open(fileName, 'r') as file:
    for line in file:
        numbers.append(int(line))
        if (int(line) == 0):
            indexZero = i
        positions.append(i)
        i += 1

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 811589153
numbersInit = numbers[:]
base = len(numbers) - 1
baseFull = base + 1
for i in range(len(numbers)):
    numbers[i] = numbers[i] % base

for n in range(10):
    for i in range(len(numbers)):
        numberToMove = numbers[i] % base
        position = positions[i]
        for j in range(len(numbers)):
            if ((positions[j] - position - 1) % baseFull in range(numberToMove)):
                positions[j] = (positions[j] - 1) % baseFull
        positions[i] = (positions[i] + numberToMove) % baseFull

def findByPosition(position):
    for i in range(len(positions)):
        if (positions[i] == position % baseFull):
            return numbersInit[i]

print(findByPosition(positions[indexZero] + 1000) +
      findByPosition(positions[indexZero] + 2000) +
      findByPosition(positions[indexZero] + 3000))
