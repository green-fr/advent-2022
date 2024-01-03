# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:36:05 2023

@author: green
"""

alphabet = '.' + ''.join(chr(i) for i in range(ord('a'), ord('z') + 1)) + ''.join(chr(i) for i in range(ord('A'), ord('Z') + 1))

def checkOneLine(line):
    width = len(line) // 2
    first = line[0 : width]
    second = line[width : 2 * width]
    for char in first:
        if (char in second):
            return alphabet.index(char)


with open('03.input.txt', 'r') as file:
    counter = 0;
    for line in file:
        counter += checkOneLine(line)
    print(counter)

print(alphabet)
