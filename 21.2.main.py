# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

import re

monkeys = {}

fileName = '21.input.txt'
with open(fileName, 'r') as file:
    for line in file:
        parsedLine = re.split(r':| |\n', line)
        if (len(parsedLine) == 4):
            monkeys[parsedLine[0]] = int(parsedLine[2])
        else:
            monkeys[parsedLine[0]] = parsedLine[2 : 5]
                
def getValue(name):
    monkey = monkeys[name]
    if (name == 'humn'):
        return name
    elif (isinstance(monkey, (int, float))):
        return monkey
    else:
        monkey0 = getValue(monkey[0])
        monkey2 = getValue(monkey[2])
        if (isinstance(monkey0, (int, float))):
            if (isinstance(monkey2, (int, float))):
                if (monkey[1] == '+'):
                    monkeys[name] = monkey0 + monkey2
                elif (monkey[1] == '-'):
                    monkeys[name] = monkey0 - monkey2
                elif (monkey[1] == '*'):
                    monkeys[name] = monkey0 * monkey2
                elif (monkey[1] == '/'):
                    monkeys[name] = monkey0 / monkey2
                return monkeys[name]
            else:
                monkeys[name][0] = monkey0
        else:
            if (isinstance(monkey2, (int, float))):
                monkeys[name][2] = monkey2
    return name

def getValueSimple(name):
    monkey = monkeys[name]
    if (isinstance(monkey, (int, float))):
        return monkey
    else:
        return name
        
monkeyRoot = monkeys['root']
print(getValue(monkeyRoot[0]))
print(getValue(monkeyRoot[2]))

def myPrint(name):
    monkey = monkeys[name]
    print(name, monkey)
    if (not isinstance(monkey, (int, float))):
        if (not isinstance(monkey[0], (int, float))):
            myPrint(monkey[0])
        if (not isinstance(monkey[2], (int, float))):
            myPrint(monkey[2])

myPrint('root')

def backProp(name, value):
    if (name == 'humn'):
        print(name, value)
        return
    monkey = monkeys[name]
    monkey0 = monkey[0]
    monkey2 = monkey[2]
    monkeys[name] = value
    isKnow0 = isinstance(monkey0, (int, float))
    # isKnow2 = isinstance(monkey2, (int, float))
    if (monkey[1] == '+'):
        if (isKnow0):
            backProp(monkey2, value - monkey0)
        else:
            backProp(monkey0, value - monkey2)
    elif (monkey[1] == '-'):
        if (isKnow0):
            backProp(monkey2, monkey0 - value)
        else:
            backProp(monkey0, value + monkey2)
    elif (monkey[1] == '*'):
        if (isKnow0):
            backProp(monkey2, value / monkey0)
        else:
            backProp(monkey0, value / monkey2)
    elif (monkey[1] == '/'):
        if (isKnow0):
            backProp(monkey2, monkey0 / value)
        else:
            backProp(monkey0, value * monkey2)

print(getValueSimple(monkeyRoot[0]))
print(getValueSimple(monkeyRoot[2]))
backProp(getValueSimple(monkeyRoot[0]), getValue(monkeyRoot[2]))
