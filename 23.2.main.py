# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green

Very inefficient version
"""

with open('23.input.txt', 'r') as file:
    counter = 0;
    lines = file.readlines()
    
monkeys = []
for i, line in enumerate(lines):
    for j in range(len(line)):
        if (line[j] == '#'):
            monkeys.append((i, j))

def getNeighbors(monkey):
    neighbors = set()
    if ((monkey[0] - 1, monkey[1]) in monkeys):
        neighbors.add('N')
    if ((monkey[0] - 1, monkey[1] - 1) in monkeys):
        neighbors.add('N')
        neighbors.add('W')
    if ((monkey[0], monkey[1] - 1) in monkeys):
        neighbors.add('W')
    if ((monkey[0] + 1, monkey[1] - 1) in monkeys):
        neighbors.add('S')
        neighbors.add('W')
    if ((monkey[0] + 1, monkey[1]) in monkeys):
        neighbors.add('S')
    if ((monkey[0] + 1, monkey[1] + 1) in monkeys):
        neighbors.add('S')
        neighbors.add('E')
    if ((monkey[0], monkey[1] + 1) in monkeys):
        neighbors.add('E')
    if ((monkey[0] - 1, monkey[1] + 1) in monkeys):
        neighbors.add('N')
        neighbors.add('E')
    return neighbors

def getNewPosition(monkey, direction):
    if (direction == 'N'):
        return (monkey[0] - 1, monkey[1])
    elif (direction == 'S'):
        return (monkey[0] + 1, monkey[1])
    elif (direction == 'W'):
        return (monkey[0], monkey[1] - 1)
    elif (direction == 'E'):
        return (monkey[0], monkey[1] + 1)
    else:
        return monkey

def getProposition(monkey, priority):
    neighbors = getNeighbors(monkey)
    if (not neighbors):
        return monkey
    for direction in priority:
        if (not direction in neighbors):
            return getNewPosition(monkey, direction)
    return monkey

def findExtremes():
    minX, minY, maxX, maxY = (1E10, 1E10, 0, 0)
    for monkey in monkeys:
        minX = min(minX, monkey[1])
        minY = min(minY, monkey[0])
        maxX = max(maxX, monkey[1])
        maxY = max(maxY, monkey[0])
    return minX, minY, maxX, maxY

def myPrint(monkeys):
    maze = []
    minX, minY, maxX, maxY = findExtremes()
    for y in range(minY, maxY + 1):
        maze.append('.' * (maxX - minX + 1))
    for monkey in monkeys:
        m = (monkey[0] - minY, monkey[1] - minX)
        maze[m[0]] = maze[m[0]][ : m[1]] + '#' + maze[m[0]][m[1] + 1 : ]
    for line in maze:
        print(line)

priority = ('N', 'S', 'W', 'E')
dirty = True
day = 0
while (dirty):
    dirty = False
    day += 1
    propositions = []
    for monkey in monkeys:
        propositions.append(getProposition(monkey, priority))
    newMonkeys = []
    for i, proposition in enumerate(propositions):
        if (propositions.count(proposition) == 1):
            newMonkeys.append(proposition)
            if (proposition != monkeys[i]):
                dirty = True
        else:
            newMonkeys.append(monkeys[i])
    monkeys = newMonkeys
    priority = priority[1 :] + (priority[0],)
    print('Day', day)
    # myPrint(monkeys)

print(day)
minX, minY, maxX, maxY = findExtremes()

print((maxX - minX + 1) * (maxY - minY + 1) - len(monkeys))
