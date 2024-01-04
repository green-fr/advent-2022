# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

import re

def findIntersection(interval1, interval2):
    if (interval1[0] <= interval2[0]):
        if (interval1[1] < interval2[0] - 1):
            return False, None
        else:
            if (interval1[1] <= interval2[1]):
                return True, (interval1[0], interval2[1])
            else:
                return True, (interval1[0], interval1[1])
    else:
        return findIntersection(interval2, interval1)
def cut(master, subMaster):
    if (master[0] < subMaster[0]):
        return (master[0], subMaster[0] - 1)
    else:
        return (subMaster[0] + 1, master[1])

class Intervals:
    yInterval = None
    intervals = None
    def __init__(self, yInterval):
        self.yInterval = yInterval
        self.intervals = {}
        for y in range(self.yInterval[0], self.yInterval[1] + 1):
            self.intervals[y] = []
    def addSensorData(self, sensor, beacon):
        distanceToBeacon = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        for y in range(self.yInterval[0], self.yInterval[1] + 1):
            distanceToLine = abs(sensor[1] - y)
            gap = distanceToBeacon - distanceToLine
            if (gap >= 0):
                interval = (sensor[0] - gap, sensor[0] + gap)
                self.addInterval(interval, y)
    def addInterval(self, intervalToAdd, y):
        dirty = True
        while (dirty):
            dirty = False
            for interval in self.intervals[y]:
                isIntersecting, union = findIntersection(interval, intervalToAdd)
                if (isIntersecting):
                    dirty = True
                    intervalToAdd = union
                    self.intervals[y] = [element for element in self.intervals[y] if element != interval]
        self.intervals[y].append(intervalToAdd)
    def getEmptySpace(self, masterInterval):
        for y in range(self.yInterval[0], self.yInterval[1] + 1):
            self.intervals[y] = sorted(self.intervals[y], key = lambda x: x[0])
            for interval in self.intervals[y]:
                if (interval[0] <= masterInterval[0] and interval[1] < masterInterval[1]):
                    return (interval[1] + 1, y)
                if (interval[0] > masterInterval[0] and interval[1] >= masterInterval[1]):
                    return (interval[0] - 1, y)

fileName = '15.input.txt'
masterInterval = (0, 4000000)
intervals = Intervals(masterInterval)
with open(fileName, 'r') as file:
    for line in file:
        print(line)
        parsedLine = re.split(r'=|,|:|\n', line)
        intervals.addSensorData((int(parsedLine[1]), int(parsedLine[3])), (int(parsedLine[5]), int(parsedLine[7])))

emptySpace = intervals.getEmptySpace(masterInterval)
print(emptySpace[1] + 4000000 * emptySpace[0])
