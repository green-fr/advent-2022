# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

# Not finished

import math

class BluePrint:
    number = None
    priceRobot = None
    best = None
    bestPath = None
    def __init__(self, parsedLine):
        self.number = int(parsedLine[1][ : -1])
        self.priceRobot = []
        self.priceRobot.append([int(parsedLine[6]), 0, 0, 0])
        self.priceRobot.append([int(parsedLine[12]), 0, 0, 0])
        self.priceRobot.append([int(parsedLine[18]), int(parsedLine[21]), 0, 0])
        self.priceRobot.append([int(parsedLine[27]), 0, int(parsedLine[30]), 0])
        self.best = 0
    def getNeededTime(self, option, stock, speed):
        neededTime = 1
        for i in range(len(self.priceRobot[option])):
            price = self.priceRobot[option]
            if (stock[i] >= price[i]):
                pass
            elif (speed[i] == 0):
                return None
            else:
                neededTime = max(neededTime, math.ceil((price[i] - stock[i]) / speed[i]) + 1)
        return neededTime
    def findBest(self, stockInit, speedInit, timeInit, path):
        options = (3, )
        if (speedInit[2] < self.priceRobot[3][2]):
            options += (2,)
        if (speedInit[1] < max(self.priceRobot[2][1], self.priceRobot[3][1])):
            options += (1,)
        if (speedInit[0] < max(self.priceRobot[1][0], self.priceRobot[2][0], self.priceRobot[3][0])):
            options += (0,)
        for i in range(len(options)):
            stock = stockInit
            speed = speedInit
            time = timeInit
            option = options[i]
            neededTime = self.getNeededTime(option, stock, speed)
            if (neededTime != None and neededTime < time):
                stock = addStock(stock, speed, neededTime)
                time -= neededTime
                speed = tuple(element + 1 if i == option else element for i, element in enumerate(speed))
                price = self.priceRobot[option]
                stock = payPrice(stock, price)
                self.findBest(stock, speed, time, path + '.' * (neededTime - 1) + str(option))
            else:
                stock = addStock(stock, speed, time)
                print(path, stock[3])
                if (self.best < stock[3]):
                    self.best = stock[3]
                    self.bestPath = path
            
def addStock(stock, speed, time):
    return tuple(stocki + speedi * time for stocki, speedi in zip(stock, speed))
def payPrice(stock, price):
    return tuple(stocki - pricei for stocki, pricei in zip(stock, price))

blueprints = []
fileName = '19.input small.txt'
with open(fileName, 'r') as file:
    for line in file:
        parsedLine = line.split(' ')
        blueprints.append(BluePrint(parsedLine))

answer = 0
import time as t
for i in range(len(blueprints)):
    blueprint = blueprints[i]
    stock = (0, 0, 0, 0)
    speed = (1, 0, 0, 0)
    time = 32
    start_time = t.time()
    blueprint.findBest(stock, speed, time, '')
    end_time = t.time()
    print(blueprint.bestPath, blueprint.best)
    answer += blueprint.best * blueprint.number
    elapsed_time = end_time - start_time
    print("Time elapsed: {:.2f} seconds".format(elapsed_time))

print(answer)
