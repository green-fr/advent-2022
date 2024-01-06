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
    if (isinstance(monkey, int)):
        return monkey
    else:
        if (monkey[1] == '+'):
            monkeys[name] = getValue(monkey[0]) + getValue(monkey[2])
            return monkeys[name]
        elif (monkey[1] == '-'):
            monkeys[name] = getValue(monkey[0]) - getValue(monkey[2])
            return monkeys[name]
        elif (monkey[1] == '*'):
            monkeys[name] = getValue(monkey[0]) * getValue(monkey[2])
            return monkeys[name]
        elif (monkey[1] == '/'):
            monkeys[name] = getValue(monkey[0]) / getValue(monkey[2])
            return monkeys[name]
        
print(getValue('root'))
