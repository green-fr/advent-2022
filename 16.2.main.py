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
bestPathes = ()
startingPoint = valveIndex['AA']
timeLimit = 26

def getBest(stillClosed, currentPlace1, currentPlace2, currentTime, currentRate, currentValue, currentPath1, currentPath2, rest1, rest2):
    global bestValue
    global bestPathes
    valueForNothing = currentValue + currentRate * (timeLimit - currentTime)
    if (valueForNothing > bestValue):
        bestValue = valueForNothing
        bestPathes = (currentPath1, currentPath2)
    if (rest1 == 0):
        currentRate += valves[currentPlace1].flowRate
        # choose 1
        for i in stillClosed:
            timeStep = prices[currentPlace1][i] + 1
            if (currentTime + timeStep <= timeLimit):
                stillClosed.remove(i)
                previousPlace = currentPlace1
                currentPlace1 = i
                rest1 = timeStep
                currentPath1 = currentPath1 + (i,)
                getBest(stillClosed, currentPlace1, currentPlace2, currentTime, currentRate, currentValue, currentPath1, currentPath2, rest1, rest2)
                currentPath1 = currentPath1[ : -1]
                rest1 = 0
                currentPlace = previousPlace
                stillClosed.add(i)
    elif (rest2 == 0):
        currentRate += valves[currentPlace2].flowRate
        # choose 2
        for i in stillClosed:
            timeStep = prices[currentPlace1][i] + 1
            if (currentTime + timeStep <= timeLimit):
                stillClosed.remove(i)
                previousPlace = currentPlace1
                currentPlace2 = i
                rest2 = timeStep
                currentPath2 = currentPath2 + (i,)
                getBest(stillClosed, currentPlace1, currentPlace2, currentTime, currentRate, currentValue, currentPath1, currentPath2, rest1, rest2)
                currentPath2 = currentPath2[ : -1]
                rest2 = 0
                currentPlace = previousPlace
                stillClosed.add(i)
    else:
        # skip one tick
        currentTime += 1
        currentValue += currentRate
        rest1 -= 1
        rest2 -= 1
        getBest(stillClosed, currentPlace1, currentPlace2, currentTime, currentRate, currentValue, currentPath1, currentPath2, rest1, rest2)
        rest2 += 1
        rest1 += 1
        currentValue -= currentRate
        currentTime -= 1

#getBest(set(nonZeroValves), startingPoint, startingPoint, 0, 0, 0, (startingPoint,), (startingPoint,), 0, 0)
#print(bestValue, bestPathes)

# Doesn't work...
