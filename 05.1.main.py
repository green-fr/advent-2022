# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

alphabet = '.' + ''.join(chr(i) for i in range(ord('a'), ord('z') + 1)) + ''.join(chr(i) for i in range(ord('A'), ord('Z') + 1))

def initStack(linesStack):
    stack = []
    nbStacks = len(linesStack[-1]) // 4
    for i in range(0, nbStacks):
        stack.append([])
    for i in range(len(linesStack) - 2, -1, -1):
        for j in range(0, nbStacks):
            char = linesStack[i][4 * j + 1]
            if (not char == ' '):
                stack[j].append(char)
    return stack

def proceedOneLine(stack, line):
    instruction = line.split(' ')
    nombre = int(instruction[1])
    stackFrom = int(instruction[3])
    stackTo = int(instruction[5])
    for i in range(0, nombre):
        stack[stackTo - 1].append(stack[stackFrom - 1][-1])
        stack[stackFrom - 1] = stack[stackFrom - 1][0 : -1]
    return stack

with open('05.input.txt', 'r') as file:
    linesStack = [];
    initialized = False
    for line in file:
        if (not initialized):
            if (line == '\n'):
                stack = initStack(linesStack)
                initialized = True
            else:
                linesStack.append(line)
        else:
            stack = proceedOneLine(stack, line)
            
    answer = ''
    for i in range(0, len(stack)):
        answer += stack[i][-1]
    print(answer)
