# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

def parsePacket(packet):
    answer = []
    level = 0
    current = ''
    for char in packet:
        if (char == '['):
            level += 1
            if (level > 1):
                current += char    
        elif (char == ']'):
            level -= 1
            if (level >= 1):
                current += char    
        elif (char == ',' and level == 1):
            answer.append(current)
            current = ''
        else:
            current += char
    if (current != ''):
        answer.append(current)
    return answer

def isList(packet):
    return (packet[0] == '[')

def comparePackets(left, right):
    if (isList(left)):
        if (isList(right)):
            parsedLeft = parsePacket(left)
            parsedRight = parsePacket(right)
            for i in range(len(parsedLeft)):
                leftLoop = parsedLeft[i]
                if (len(parsedRight) < i + 1):
                    return 1
                else:
                    rightLoop = parsedRight[i]
                compareLoop = comparePackets(leftLoop, rightLoop)
                if (compareLoop == -1):
                    return -1
                elif (compareLoop == 1):
                    return 1
            if (len(parsedRight) > len(parsedLeft)):
                return -1
            else:
                return 0
        else:
            return comparePackets(left, '[' + right + ']')
    else:
        if (isList(right)):
            return comparePackets('[' + left + ']', right)
        else:
            parsedLeft = int(left)
            parsedRight = int(right)
            if (parsedLeft < parsedRight):
                return -1
            elif (parsedLeft == parsedRight):
                return 0
            else:
                return 1

def addToSorted(sortedPackets, line):
    if (len(sortedPackets) == 0):
        return [line], 0
    lowerBound = 0
    upperBound = len(sortedPackets)
    while (lowerBound < upperBound):
        compareWith = (lowerBound + upperBound - 1) // 2
        result = comparePackets(line, sortedPackets[compareWith])
        if (result == -1):
            upperBound = compareWith
        else:
            lowerBound = compareWith + 1
    answer = sortedPackets[ : lowerBound] + [line] + sortedPackets[lowerBound : ]
    return answer, lowerBound
    

with open('13.input.txt', 'r') as file:
    sortedPackets = []
    for line in file:
        if (line != '\n'):
            sortedPackets, index = addToSorted(sortedPackets, line[ : -1])
sortedPackets, index2 = addToSorted(sortedPackets, '[[2]]')
sortedPackets, index6 = addToSorted(sortedPackets, '[[6]]')
#print(sortedPackets)
print((index2 + 1) * (index6 + 1))
