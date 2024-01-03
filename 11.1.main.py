# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

class Monkey:
    items = None
    operation = None
    operand = None
    divisibilityTest = None
    testTrue = None
    testFalse = None
    counter = 0
    def __init__(self):
        self.items = []
    def loadStartingItems(self, itemsLine):
        for item in itemsLine:
            self.items.append(int(item[0 : -1]))
    def loadOperation(self, operationLine):
        operation = operationLine[6]
        operand = operationLine[7][ : -1]
        if (operand == 'old'):
            self.operation = '^'
            self.operand = 2
        else:    
            self.operation = operation
            self.operand = int(operand)
    def loadTest(self, testLine):
        self.divisibilityTest = int(testLine[5][ : -1])
    def loadTrue(self, trueLine):
        self.testTrue = int(trueLine[9][ : -1])
    def loadFalse(self, falseLine):
        self.testFalse = int(falseLine[9][ : -1])
    def dump(self):
        print(self.items, self.counter)
    def addItem(self, item):
        self.items.append(item)
    def play(self):
        if (len(self.items) == 0):
            return None, None
        self.counter += 1
        item = self.items[0]
        self.items = self.items[1 : ]
        if (self.operation == '+'):
            item += self.operand
        elif (self.operation == '-'):
            item -= self.operand
        elif (self.operation == '*'):
            item *= self.operand
        elif (self.operation == '/'):
            item /= self.operand
        elif (self.operation == '^'):
            item **= self.operand
        item //= 3
        test = (item % self.divisibilityTest == 0)
        if (test):
            return item, self.testTrue
        else:
            return item, self.testFalse
        

monkeys = []
with open('11.input.txt', 'r') as file:
    for line in file:
        parsedLine = line.split(' ')
        if (parsedLine[0] == 'Monkey'):
            monkeys.append(Monkey())
        elif (parsedLine[0] == '\n'):
            pass
        elif (parsedLine[2] == 'Starting'):
            monkeys[-1].loadStartingItems(parsedLine[4 : ])
        elif (parsedLine[2] == 'Operation:'):
            monkeys[-1].loadOperation(parsedLine)
        elif (parsedLine[2] == 'Test:'):
            monkeys[-1].loadTest(parsedLine)
        elif (parsedLine[5] == 'true:'):
            monkeys[-1].loadTrue(parsedLine)
        elif (parsedLine[5] == 'false:'):
            monkeys[-1].loadFalse(parsedLine)

for i in range(0, len(monkeys)):
    monkeys[i].dump()
for r in range(0, 20):
    print('Round: ', r)
    for i in range(0, len(monkeys)):
        newItem, newMonkey = monkeys[i].play()
        while (newItem != None):
            monkeys[newMonkey].addItem(newItem)
            newItem, newMonkey = monkeys[i].play()
    for i in range(0, len(monkeys)):
        monkeys[i].dump()
counters = []
for i in range(0, len(monkeys)):
    counters.append(monkeys[i].counter)
sortedCounters = sorted(counters)
print(sortedCounters[-1] * sortedCounters[-2])
