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
    print(left, right)
    if (isList(left)):
        if (isList(right)):
            parsedLeft = parsePacket(left)
            parsedRight = parsePacket(right)
            for i in range(len(parsedLeft)):
                leftLoop = parsedLeft[i]
                if (len(parsedRight) < i + 1):
                    print(1)
                    return 1
                else:
                    rightLoop = parsedRight[i]
                compareLoop = comparePackets(leftLoop, rightLoop)
                if (compareLoop == -1):
                    print(-1)
                    return -1
                elif (compareLoop == 1):
                    print(1)
                    return 1
            if (len(parsedRight) > len(parsedLeft)):
                print(-1)
                return -1
            else:
                print(0)
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
                print(-1)
                return -1
            elif (parsedLeft == parsedRight):
                print(0)
                return 0
            else:
                print(1)
                return 1

with open('13.input.txt', 'r') as file:
    counter = 0;
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        left = lines[i][ : -1]
        right = lines[i + 1][ : -1]
        result = comparePackets(left, right)
        #print(left, right, result)
        if (result < 1):
            print(i // 3 + 1)
            counter += (i // 3 + 1)

print(counter)
