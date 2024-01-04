# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

import re

def findIntersection(interval1, interval2):
    if (interval1[0] <= interval2[0]):
        if (interval1[1] < interval2[0]):
            return False, None
        else:
            if (interval1[1] <= interval2[1]):
                return True, (interval1[0], interval2[1])
            else:
                return True, (interval1[0], interval1[1])
    else:
        return findIntersection(interval2, interval1)

class Intervals:
    y = 2000000
    intervals = None
    beacons = None
    def __init__(self):
        self.intervals = []
        self.beacons = []
    def addSensorData(self, sensor, beacon):
        distanceToBeacon = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        distanceToLine = abs(sensor[1] - self.y)
        gap = distanceToBeacon - distanceToLine
        if (gap >= 0):
            interval = (sensor[0] - gap, sensor[0] + gap)
            print(sensor, beacon, interval)
            self.addInterval(interval)
        else:
            print(sensor, beacon, None)
        if (beacon[1] == self.y):
            self.addBeacon(beacon)
    def addInterval(self, intervalToAdd):
        print(self.intervals, intervalToAdd)
        dirty = True
        while (dirty):
            dirty = False
            for interval in self.intervals:
                isIntersecting, intersection = findIntersection(interval, intervalToAdd)
                if (isIntersecting):
                    dirty = True
                    intervalToAdd = intersection
                    self.intervals = [element for element in self.intervals if element != interval]
        self.intervals.append(intervalToAdd)
        print(self.intervals)
    def addBeacon(self, beacon):
        self.beacons.append(beacon[0])
    def getLength(self):
        length = 0
        for interval in self.intervals:
            length += interval[1] - interval[0] + 1 - len(set(self.beacons))
        return length

intervals = Intervals()
fileName = '15.input.txt'
with open(fileName, 'r') as file:
    for line in file:
        parsedLine = re.split(r'=|,|:|\n', line)
        intervals.addSensorData((int(parsedLine[1]), int(parsedLine[3])), (int(parsedLine[5]), int(parsedLine[7])))
print(intervals.getLength())
