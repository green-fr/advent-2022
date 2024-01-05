# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

class Valve:
    name = None
    flowRate = None
    tunnels = None
    isOpen = False
    def __init__(self, line):
        parsedLine = line.split(' ')
        self.name = parsedLine[1]
        parsedFlowRate = parsedLine[4].split('=')
        self.flowRate = int(parsedFlowRate[1][ : - 1])
        self.tunnels = []
        for i in range(9, len(parsedLine)):
            self.tunnels.append(parsedLine[i][ : -1])

valves = []
valveIndex = {}
fileName = '16.input small.txt'
with open(fileName, 'r') as file:
    index = 0
    for line in file:
        valve = Valve(line)
        valves += [valve]
        valveIndex[valve.name] = index
        index += 1

n = len(valves)
prices = [[-1 for j in range(n)] for i in range(n)]
for i in range(n):
    prices[i][i] = 0
    for wave in range(n):
        for j in range(n):
            if (prices[i][j] == wave):
                neighbours = valves[j].tunnels
                for k in range(len(neighbours)):
                    index = valveIndex[neighbours[k]]
                    if (prices[i][index] == -1):
                        prices[i][index] = wave + 1

nonZeroValves = []
for i in range(n):
    if (valves[i].flowRate != 0):
        nonZeroValves += [i]

bestValue = 0
bestPath = None
startingPoint = valveIndex['AA']
timeLimit = 30

def getBest(stillClosed, currentPlace, currentTime, currentRate, currentValue, currentPath):
    global bestValue
    global bestPath
    valueForNothing = currentValue + currentRate * (timeLimit - currentTime)
    if (valueForNothing > bestValue):
        bestValue = valueForNothing
        bestPath = currentPath
    for i in stillClosed:
        timeStep = prices[currentPlace][i] + 1
        if (currentTime + timeStep <= timeLimit):
            stillClosed.remove(i)
            previousPlace = currentPlace
            currentPlace = i
            currentValue += currentRate * timeStep
            currentRate += valves[i].flowRate
            currentTime += timeStep
            currentPath = currentPath + (i,)
            getBest(stillClosed, currentPlace, currentTime, currentRate, currentValue, currentPath)
            currentPath = currentPath[ : -1]
            stillClosed.add(i)
            currentTime -= timeStep
            currentRate -= valves[i].flowRate
            currentValue -= currentRate * timeStep
            currentPlace = previousPlace

getBest(set(nonZeroValves), startingPoint, 0, 0, 0, (startingPoint,))
print(bestValue, bestPath)
