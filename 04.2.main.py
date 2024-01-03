# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

alphabet = '.' + ''.join(chr(i) for i in range(ord('a'), ord('z') + 1)) + ''.join(chr(i) for i in range(ord('A'), ord('Z') + 1))

def checkOneLine(line):
    a = line.split(',')
    b = [int(element) for element in a[0].split('-')]
    c = [int(element) for element in a[1].split('-')]
    if (b[0] <= c[0] <= b[1]) or (c[0] <= b[0] <= c[1]):
        return 1
    else:
        return 0
        

with open('04.input.txt', 'r') as file:
    counter = 0;
    for line in file:
        counter += checkOneLine(line)
    print(counter)
